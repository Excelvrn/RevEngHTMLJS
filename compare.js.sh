clear
declare WDIR="/home/excelvrn/ArtDentalPro"
declare fn="index.html"
declare js="component---src-pages-index-js-cf481975c837ecd269ef.js"
#/home/excelvrn/ArtDentalPro/Work.120521/index.html

declare work="Work.120521"
declare saved="saved/s.140521"
declare saved2="saved/go20nikdu"
declare common="public_html"
#declare dir2="asdf"

declare file1=$WDIR/$work/$fn
declare file2=$WDIR/$saved/$common/$fn
declare file3=$WDIR/$saved2/$common/$fn

#echo $file1
#head $file1
#echo $file2
#head $file2
echo $PWD
cd res/
diff -a $file1 $file2 > work.saved.html.out
echo "--------------------------------------------------------------------------------"
echo "----------------------------------------"
echo "--------------------------------------------------------------------------------"
echo "----------------------------------------"
echo "--------------------------------------------------------------------------------"
diff -a $file1 $file3 > work.g20.html.out
echo "--------------------------------------------------------------------------------"
echo "----------------------------------------"
echo "--------------------------------------------------------------------------------"
echo "----------------------------------------"
echo "--------------------------------------------------------------------------------"

declare file4=$WDIR/$work/$js
declare file5=$WDIR/$saved/$common/$js
declare file6=$WDIR/$saved2/$common/$js
echo "--------------------------------------------------------------------------------"
echo "----------------------------------------"
echo $file4 
echo $file5
echo "--------------------------------------------------------------------------------"
echo "----------------------------------------"
echo "--------------------------------------------------------------------------------"
diff -a $file4 $file5 > work.saved.js.out
echo "--------------------------------------------------------------------------------"
echo "----------------------------------------"
echo $file4 
echo $file6
echo "--------------------------------------------------------------------------------"
echo "----------------------------------------"
echo "--------------------------------------------------------------------------------"
diff -a $file4 $file6 > work.g20.js.out
echo "--------------------------------------------------------------------------------"
echo "----------------------------------------"
echo $file5
echo $file6
echo "--------------------------------------------------------------------------------"
echo "----------------------------------------"
echo "--------------------------------------------------------------------------------"
diff -a $file5 $file6 > saved.g20.js.out