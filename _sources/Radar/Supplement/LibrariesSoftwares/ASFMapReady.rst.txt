.. _Section-ASFMapReadyLibrariesSoftwaresSupplementRadar:

ASF MapReady
=====================


Alaska Satellite Facility

简介
-----------------------

`MapReady <https://www.asf.alaska.edu/software-tools/#mapready>`_ 是由 ASF 开发的遥感数据处理工具, 主要用于处理各种SAR数据, 尤其适合处理 CEOS 格式的数据, 其源码可以在 `这里 <https://github.com/asfadmin/ASF_MapReady>`_ 获得. ASF MapReady 支持 ERS Level0 数据读取, 不支持 Sentinel Level0 数据读取.



.. note::
   由 ASF MapReady 中的源码可知, 暂不支持 Sentinel Level0 级数据, 具体参见 `src/libasf_import/import_sentinel.c` 文件中的 :func:`import_sentinel` 函数::

   if (strcmp_case(productType, "RAW") == 0)
      asfPrintError("Product type 'RAW' currently not supported!\n");
   else if (strcmp_case(productType, "SLC") == 0 ||
      strcmp_case(productType, "GRD") == 0)


安装 ASF MapReady
-----------------------

Ubuntu下配置安装
~~~~~~~~~~~~~~~~~~~~~~

安装步骤如下:

1. 安装依赖:

   ::

       sudo apt install gcc g++ bison flex libcunit1-dev libexif-dev libfftw3-dev libgdal-dev libgeotiff-dev libglade2-dev libglib2.0-dev libgsl-dev libgtk2.0-dev libjpeg-dev libpng-dev libproj-dev libshp-dev libtiff5-dev libxml2-dev

2. 配置安装目录: ``./configure --prefix=your_installation_path`` , 注意更改为自己的安装目录, 如 ``/mnt/e/sfw/sar/ASF_MapReady``

3. 构建: ``make`` 或多线程构建 ``make -j16``

4. 安装: ``make install``

5. 添加环境变量 ``export PATH=your_installation_path/bin:$PATH``

安装完成后, 在终端输入 ``asf_mapready --help`` 可查看帮助并验证安装是否成功, 若安装成功, 则可以看到如下提示:::

    :~$ asf_mapready --help

    Tool name:
       asf_mapready

    Usage:
       asf_mapready [-create] [-input <inFile>] [-output <outFile>]
                    [-tmpdir <dir>] [-log <logFile>] [-quiet] [-license]
                    [-version] [-help]
                    <config_file>

    Description:
       This program can ingest level one CEOS and GeoTIFF format data, calibrate
       it to various radiometries, perform polarimetric decompositions, perform
       Faraday Rotation correction, perform terrain correction, geocode it, and
       then export it to a variety of graphics file formats. The user is able to
       control how asf_mapready dictates the processiong flow by creating a
       configuration file, which must then be edited, which is fed into
       asf_mapready when it is called.
    :
    :



ASF MapReady 源码分析
------------------------

数据读取
~~~~~~~~~~~~~~~~~~~~~~~~~

``asf_view --> read --> read_ceos/envi/seasat/terrasar/uavsar/tiff...``


通过分析源码可知, :class:`ImageInfo` 结构体是和读取显示图像相关的结构体, 在 `asf_view.h` 中定义了 :class:`ImageInfo` 指针类型的两个变量( :attr:`curr` , :attr:`mask` )和一个数组( :attr:`image_info` ) ::

    // Can hold five images
    #define MAX_IMAGES 5
    extern ImageInfo image_info[MAX_IMAGES];
    // "curr" always points to the currently being displayed image info
    extern ImageInfo *curr;
    extern ImageInfo *mask;
    extern int current_image_info_index;
    extern int n_images_loaded;

其中, 数组 :attr:`image_info` 存储多个图像 :class:`ImageInfo` 结构体, :attr:`curr` 指针总是指向当前要显示的图像信息. :class:`ImageInfo` 结构体中存储了待读取和显示图像的所有信息, 可以使用 `cache.c` 文件中的 :func:`get_pixel` 函数读取. :class:`ImageInfo` 结构体成员如下.

.. cpp:struct:: ImageInfo

   typedef struct {
        int nl, ns; // number of lines(azimuth), number of samples(range)

        meta_parameters *meta; // meta parameters

        CachedImage *data_ci; //

        BandConfig band_cfg;

        ImageStats stats;

        ImageStatsRGB stats_r;

        ImageStatsRGB stats_g;

        ImageStatsRGB stats_b;

        char *filename;

        char *data_name;

        char *meta_name;

   } ImageInfo;


其中 :class:`CachedImage` 也是一个结构体, 其中存储着待读取图像的信息以及读取方法.

.. cpp:struct:: CachedImage

   typedef struct {
   // Here is the ImageCache stuff.  The global ImageCache that holds the loaded image is "data_ci".  This is all private data.
      int nl, ns;               // Image dimensions.

      ClientInterface *client;  // pointers to data read implementations

      int n_tiles;              // Number of tiles in memory

      int reached_max_tiles;    // Have we loaded as many tiles as we can?

      int rows_per_tile;        // Number of rows in each tile

      int entire_image_fits;    // TRUE if we can load the entire image

      int *rowstarts;           // Row numbers starting each tile

      unsigned char **cache;    // Cached values (floats, unsigned chars ...)

      int *access_counts;       // Updated when a tile is accessed

      int n_access;             // used to find oldest tile

      ssv_data_type_t data_type;// type of data we have

      meta_parameters *meta;    // metadata -- don't own this pointer

      ImageStats *stats;        // not owned by us, not populated by us

      ImageStatsRGB *stats_r;   // not owned by us, not populated by us

      ImageStatsRGB *stats_g;   // not owned by us, not populated by us

      ImageStatsRGB *stats_b;   // not owned by us, not populated by us

    } CachedImage;

其中 :class:`ClientInterface` 也是一个结构体, 其中存储着待读取图像的方法.

.. cpp:struct:: ClientInterface

   typedef struct {

      ReadClientFn *read_fn;

      ThumbFn *thumb_fn;

      FreeFn *free_fn;

      void *read_client_info;

      ssv_data_type_t data_type;

      int require_full_load;

   } ClientInterface;

如对于CEOS格式, :attr:`read_fn` 指向函数 :func:`read_ceos_client`, 其参数如下:

.. cpp:function:: int read_ceos_client(int row_start, int n_rows_to_get, void *dest_void, void *read_client_info, meta_parameters *meta, int data_type)

   - :attr:`row_start`  读取起始行(azimuth)
   - :attr:`n_rows_to_get`  读取行数(azimuth)
   - :attr:`dest_void`  输出缓存指针
   - :attr:`read_client_info` 元信息指针
   - :attr:`meta` 元信息指针
   - :attr:`data_type` 数据类型


:attr:`read_fn` 指针指向的函数被 `cache.c` 文件中的 :func:`get_pixel` 函数调用, 格式如下::

   self->client->read_fn(rs, rows_to_get, (void*)(self->cache[spot]),
          self->client->read_client_info, self->meta, self->client->data_type);


函数 :func:`get_pixel` 入口参数如下

.. cpp:function:: static unsigned char *get_pixel(CachedImage *self, int line, int samp)

   - :attr:`self` CachedImage 指针
   - :attr:`line` 像素所在行
   - :attr:`samp` 像素所在列

函数 :func:`get_pixel` 被函数 :func:`cached_image_get_pixel` 调用, 函数 :func:`cached_image_get_pixel` 被函数 :func:`cached_image_new_from_file` 调用, 函数 :func:`cached_image_new_from_file` 又被函数 :func:`read_file` 调用. 总结调用如下


.. note::
   ASF MapReady读取数据函数调用顺序为: :func:`main` --> :func:`on_new_button_clicked` --> :func:`new_file` --> :func:`load_file` --> :func:`load_file_banded` --> :func:`load_file_banded_imp` --> :func:`read_file` --> :func:`cached_image_new_from_file` --> :func:`cached_image_get_pixel` --> :func:`get_pixel` --> :attr:`read_fn` 指向的函数 (如 :func:`read_ceos_client`).



ASF MapReady 应用举例
-----------------------

数据导入
~~~~~~~~~~~~~~~~~~~~~~~~~~

在终端输入 ``asf_import --help`` 可查看帮助,



导出 ERS2 Level0 级数据
^^^^^^^^^^^^^^^^^^^^^^^^






