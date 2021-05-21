clear
declare WDIR="/home/excelvrn/ArtDentalPro"
declare fn="index.html"
declare js="component---src-pages-index-js-cf481975c837ecd269ef.js"
declare options=" --suppress-common-lines -y" 
$options
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
diff -a $file1 $file2 $options > work.saved.html.out
echo "--------------------------------------------------------------------------------"
echo "----------------------------------------"
echo "--------------------------------------------------------------------------------"
echo "----------------------------------------"
echo "--------------------------------------------------------------------------------"
diff -a $file1 $file3 $options> work.g20.html.out
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
diff -a $file4 $file5 $options> work.saved.js.out
echo "--------------------------------------------------------------------------------"
echo "----------------------------------------"
echo $file4 
echo $file6
echo "--------------------------------------------------------------------------------"
echo "----------------------------------------"
echo "--------------------------------------------------------------------------------"
diff -a $file4 $file6 $options> work.g20.js.out
echo "--------------------------------------------------------------------------------"
echo "----------------------------------------"
echo $file5
echo $file6
echo "--------------------------------------------------------------------------------"
echo "----------------------------------------"
echo "--------------------------------------------------------------------------------"
diff -a $file5 $file6 $options> saved.g20.js.out

########################
###### J ###### S ######
########################

#component---src-pages-doctors-butkevich-maxim-alexandrovich-js-86f43c3f6e3bf327c4ed.js
#declare js1="component---src-pages-doctors-chkv-js-89a010f6088998f8ae05.js"
declare comp1="component---src-pages-doctors-"
declare comp2="-js-89a010f6088998f8ae05.js"
declare js1="chkv"
declare js2="skovv"
declare fjs1=$WDIR/$work/$comp1$js1$comp2
declare fjs2=$WDIR/$work/$comp1$js2$comp2
echo "--------------------------------------------------------------------------------"
echo "----------------------------------------"
echo $fjs1
echo $fjs2
echo "--------------------------------------------------------------------------------"
echo "----------------------------------------"
echo "--------------------------------------------------------------------------------"
diff  $fjs1 $fjs2 > $js1.$js2.js.out $options

##########################################
###### H ###### T ###### M ###### L ######
##########################################

#component---src-pages-doctors-butkevich-maxim-alexandrovich-js-86f43c3f6e3bf327c4ed.js
#declare js1="component---src-pages-doctors-chkv-js-89a010f6088998f8ae05.js"
declare comp1="doctors"
declare js1="chkv"
declare js2="skovv"
declare fjs1=$WDIR/$work/$comp1/$js1/index.html
declare fjs2=$WDIR/$work/$comp1/$js2/index.html
echo "--------------------------------------------------------------------------------"
echo "----------------------------------------"
echo $fjs1
echo $fjs2
echo "--------------------------------------------------------------------------------"
echo "----------------------------------------"
echo "--------------------------------------------------------------------------------"
diff  $fjs1 $fjs2 > $js1.$js2.html.out $options
