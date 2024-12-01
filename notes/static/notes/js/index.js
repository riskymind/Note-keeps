const formModal=document.querySelector('.add-modal');
const modalOpenButton=document.querySelectorAll('.add');

modalOpenButton.forEach((item) => {
    item.addEventListener('click',()=>{
        formModal.style.display="block"
    })
})

const closeModal=(id)=>{
    let el =document.getElementById(id);

    el.style.display="none";
}