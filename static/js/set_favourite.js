const favs=document.querySelectorAll(".favourite_heart");
favs.forEach(fav=>{
    console.log()
   if(fav.dataset.fav=="yes"){
    fav.style.color="red";
   }
   else{
    fav.style.color="black";
   }
})
favs.forEach(fav=>{
    fav.addEventListener("click",()=>{
        fav.style.color="red";
    })
})