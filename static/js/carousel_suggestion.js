const firstCont=document.querySelector("#fr_item")
const secondCont=document.querySelector("#sc_item")
const thirdCont=document.querySelector("#th_item");
const frImgs=document.querySelectorAll(".img_fr_it")
const scImgs=document.querySelectorAll(".img_sc_it")
const thImgs=document.querySelectorAll(".img_th_it")
const frFrm=document.querySelectorAll(".frm_fr")
const scFrm=document.querySelectorAll(".frm_sc")
const thFrm=document.querySelectorAll(".frm_th")
const next=document.getElementById("next_btn_sg");
const prev=document.getElementById("prev_btn_sg");


var indexFr=0;
var indexSc=1;
var indexTh=2;
showCarouselSuggestion()
function disableImgs(){
    for(let i=0; i<frImgs.length;i++){
        frImgs[i].classList.add("disable");  
       frImgs[i].classList.remove("active");
       scImgs[i].classList.add("disable");  
       scImgs[i].classList.remove("active");
       thImgs[i].classList.add("disable");  
       thImgs[i].classList.remove("active");
    }
}
function disableForm(){
    for(let i=0; i<frFrm.length;i++){
    frFrm[i].classList.add("disable");  
    frFrm[i].classList.remove("active");
    scFrm[i].classList.add("disable");  
    scFrm[i].classList.remove("active");
    thFrm[i].classList.add("disable");  
    thFrm[i].classList.remove("active");}
}

function showCarouselSuggestion(){
    disableImgs()
    disableForm();
   frImgs[indexFr].classList.add("active")
   scImgs[indexSc].classList.add("active")
   thImgs[indexTh].classList.add("active")
   frFrm[indexFr].classList.add("active")
   scFrm[indexSc].classList.add("active")
   thFrm[indexTh].classList.add("active")
   

}
next.addEventListener("click",()=>{
    console.log("click")
    indexFr=indexSc;
    indexSc=indexTh;
    indexTh++;
    if(indexTh==frImgs.length){
        indexTh=0;
    }
   
    showCarouselSuggestion();
})
 prev.addEventListener("click",()=>{
    indexTh=indexSc;
    indexSc=indexFr
    indexFr--;
    if(indexFr<0){
    indexFr=frImgs.length-1;
     }
     showCarouselSuggestion()
 })