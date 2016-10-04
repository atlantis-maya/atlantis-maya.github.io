/*
关于图片自己切换的代码
 */
        setInterval(test,3000);
       //var array=new Array();
        var index=0;
        var array= new Array("images/1.jpg","images/2.jpg","images/3.jpg","images/4.jpg","images/5.jpg","images/6.jpg","images/7.jpg");
        function test()
        { 
            var myimg=document.getElementById("imgs");
            if(index==array.length-1)
            { 
                index=0; 
            }else{ 
                index++;
                 }
            myimg.src="static"+"/"+array[index];
        }