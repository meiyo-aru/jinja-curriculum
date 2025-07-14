window.onload = function(){
    
    academic_training = document.querySelectorAll(".list-item")
    collapsed = '-15px'
    visible = '-70px'
    
    window.matchMedia('(max-width: 768px)').addEventListener('change', () => {
        see_more = document.querySelectorAll('.see-more')
        see_more.forEach(element => {
            if(window.matchMedia('(max-width: 768px)').matches){
                element.style.right = ''
            } else {
                element.style.right = collapsed
            }
        });
    })

    academic_training.forEach(element => {
        element.addEventListener("mouseenter", () => { // when mouse enter the container of academic_trainings show the .see-more
            const width = window.matchMedia('(min-width: 768px)').matches
            if(width){
                see_more = element.querySelector('.see-more')
                see_more.style.right = visible
            }
        })
        element.addEventListener("mouseleave", () => { // when mouse leave the container of academic_trainings collapse the .see-more
            const width = window.matchMedia('(min-width: 768px)').matches
            if(width){
                see_more = element.querySelector('.see-more')
                see_more.style.right = collapsed
            }
        })
        element.querySelector('.see-more').addEventListener("click", () => { // when click in .see-more element
            information_container = element.parentNode.querySelector('.information-container') // get the parent element and search for the .resume-information-container between your childs
            if (!information_container.querySelector('.see-more')){ // verify if exists .see-more in the information_container
                information_container.innerHTML += '<div class="">OOOOOOPAAA</div>' // add see more element
                element.querySelector('.see-more').innerHTML = 'Ver menos' // change the text of see-more
                collapsed = '90px' // compensation for 'Ver menos' be more bigger than 'Ver mais'
            } else {
                information_container.querySelector('.see-more').remove() // remove the see-more element
                element.querySelector('.see-more').innerHTML = 'Ver mais' // change the text of see-more
                collapsed = '80px' // back to normal value
            }
        })
        
    });
    
}
