const btns_delete=document.querySelectorAll(".delete_fav")
const ul=document.getElementsByTagName("ul")

btns_delete.forEach(button=> {
    button.addEventListener("click",()=>{

       var selectedElement=button.getAttribute("value");
        deleteLi=document.getElementById(selectedElement)
       deleteLi.classList.add("disable")
    
    })
    
});