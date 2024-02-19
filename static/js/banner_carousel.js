const items=document.querySelectorAll(".banner_pic")
const containerBanner=document.querySelector(".container_banner")
const bannerPictures=document.querySelectorAll(".banner_pic")
const secondCarouselPictures=document.querySelectorAll(".second_pic")
const buttonCarouselHtml = Array.from(items, () => {
    return `<li class="carousel_button"></li>`;
  });
    containerBanner.insertAdjacentHTML(
      "beforeend",
      `
          <div class="wrapper_btn_carousel_bannner">
          <ul>
              ${buttonCarouselHtml.join("")}
              </ul>
          </div>
      `
    );
const buttonsCarousel=document.querySelectorAll(".carousel_button")
var prevIndex=-1;
select_btn()
function select_btn(){
    viewSelectedItemCarousel(prevIndex,0,bannerPictures);
    viewSelectedItemCarousel(prevIndex,0,secondCarouselPictures);
    
  buttonsCarousel.forEach((button,index)=> {
    button.addEventListener("click",(ev)=>{
        viewSelectedItemCarousel(prevIndex,index,bannerPictures);
        viewSelectedItemCarousel(prevIndex,index,secondCarouselPictures);
        disableBackground()
        button.classList.add("selected_button")
        prevIndex=index;
    })
    
  });
}
function disableBackground(){
    buttonsCarousel.forEach(button=> {
        button.classList.remove("selected_button");
    })
}

function disablePicturesCarousel(slides){
    slides.forEach(slide=>{
        slide.classList.remove("view_item_banner");
        slide.classList.remove("transition_slide");
    })
}

function viewSelectedItemCarousel(prevIndex,index, slidesCarousel){
    disablePicturesCarousel(slidesCarousel);
    slidesCarousel[index].classList.add("view_item_banner");
    if(prevIndex>0 && prevIndex!==index){
    slidesCarousel[prevIndex].classList.toggle("transition_slide");}
    
}

