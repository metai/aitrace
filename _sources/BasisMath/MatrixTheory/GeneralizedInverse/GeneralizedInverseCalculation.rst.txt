.. _Section-GeneralizedInverseCalculation:

广义逆计算
=====================


Hermite标准形计算 {1}-逆 和 {1,2}-逆
-------------------------------------




满秩分解法
----------------

设 :math:`{\bm A} \in {\mathbb C}_r^{m\times n} (r>0)` , 若满秩分解为 :math:`{\bm A}_r^{m\times n} = {\bm F}_r^{m\times r} {\bm G}_r^{r\times n}` , 则有

#. :math:`{\bm G}^{(1)}{\bm F}^{(i)} \in {\bm A}\{i\} (i=1,2,3)`   
#. :math:`{\bm G}^{(i)}{\bm F}^{(1)} \in {\bm A}\{i\} (i=1,2,4)` 
#. :math:`{\bm G}^{(1)}{\bm F}^{+} \in {\bm A}\{1,2,3\}` 
#. :math:`{\bm G}^{+}{\bm F}^{(1)} \in {\bm A}\{1,2,4\}` 
#. :math:`{\bm A}^+ = {\bm G}^+{\bm F}^{(1,3)} = {\bm G}^{(1,4)}{\bm F}^+` 
#. :math:`{\bm A}^+ = {\bm G}^+{\bm F}^+ = {\bm G}^H({\bm G}{\bm G}^H)^{-1} ({\bm F}^H {\bm F})^{-1}{\bm F}^H = {\bm G}^H({\bm F}^H{\bm F}{\bm G}{\bm G}^H)^{-1}{\bm F}^H = {\bm G}^H({\bm F}^H{\bm A}{\bm G}^H)^{-1}{\bm F}^H`     

