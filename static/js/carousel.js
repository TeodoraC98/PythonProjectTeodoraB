
let index = 0;
var items = document.getElementsByClassName("item_carousel_img");
var smallPic=document.getElementsByClassName("small_pic")
const onSidePic=document.querySelectorAll("smallPic")
const nextBtn=document.querySelector("#next_btn")
const prevBtn=document.querySelector("#prev_btn")
var timer;
 showCarousel();
 selectPic();
function showCarousel() {
   nextImage();
  timer = setTimeout(showCarousel,2000)
}

function setBlurry(){
  let i;
  for (i = 0; i < smallPic.length; i++) {
    smallPic[i].classList.toggle("blurry");  
  }
}
function disableItemsCarousel(){
  let i;
  for (i = 0; i < items.length; i++) {
    items[i].classList.add("disable");  
    items[i].classList.remove("active");
    smallPic[i].style.filter = 'blur(2.5px)';
  }

}
function selectPic(){
  for(let i=0; i < smallPic.length;i++){
  smallPic[i].addEventListener("click",()=>{
    disableItemsCarousel();
    stopTimer();
    items[i].classList.remove("disable");    
    items[i].classList.add("active"); 
    index=i;
    smallPic[i].style.filter = 'blur(0)';
   })
  }
}
function nextImage(){
  disableItemsCarousel();
  index++;
  if (index >= items.length) {index = 0}  
  items[index].classList.remove("disable");    
  items[index].classList.add("active"); 
  smallPic[index].style.filter = 'blur(0)';
 
}
function stopTimer(){
  if(timer){
    clearTimeout(timer);
    timer=0;
  }
}
function nextItem(){
  stopTimer();
  nextImage();
}
function prevItem(){
  stopTimer();
  disableItemsCarousel();
  index--;
  if (index < 0) {index = items.length-1}    
  items[index].classList.add("active"); 
  smallPic[index].style.filter = 'blur(0)';
}

nextBtn.addEventListener("click",()=>{
  nextItem();
})
prevBtn.addEventListener("click",()=>{
  prevItem();
})