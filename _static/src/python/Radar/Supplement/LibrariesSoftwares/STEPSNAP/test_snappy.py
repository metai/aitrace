import snappy
print('snappy.__file__:', snappy.__file__)


from snappy import ProductIO, Band


productfile = '/mnt/d/DataSets/sar/Sentinel/S1A_S1_RAW__0SDV_20191018T123114_20191018T123140_029513_035BC3_9A2A.zip'
productfile = '/mnt/d/DataSets/sar/GF3/GF3_MDJ_UFS_710752_E120.2_N14.8_20180825_L1B_DH_L10003456147/GF3_MDJ_UFS_710752_E120.2_N14.8_20180825_L1B_DH_L10003456147.tiff'
product = ProductIO.readProduct(productfile)

bands = product.getBands()

# array = bands.getRasterData().getElems()

band = Band()
rasterData = band.createCompatibleRasterData()
readRasterData(0, 0, band.getRasterWidth(), band.getRasterHeight(), rasterData)
array = rasterData.getElems()

print(array)
