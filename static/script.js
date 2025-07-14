window.onload = function(){
    
    academic_training = document.querySelectorAll(".list-item")
    collapsed = -10
    visible =  -80


    // // verify if is desktop or mobile and manipulate the position of .see-more elements
    // window.matchMedia('(max-width: 768px)').addEventListener('change', () => { 
    //     see_more = document.querySelectorAll('.see-more')
    //     see_more.forEach(element => {
    //         if(window.matchMedia('(max-width: 768px)').matches){
    //             element.style.right = ''
    //         } else {
    //             element.style.right = collapsed + 'px'
    //         }
    //     });
    // })  
    // window.matchMedia('(min-width: 768px)').addEventListener('change', () => { 
    //     see_more = document.querySelectorAll('.see-more')
    //     see_more.forEach(element => {
    //         if(window.matchMedia('(max-width: 768px)').matches){
    //             element.style.right = ''
    //         } else {
    //             element.style.right = collapsed + 'px'
    //         }
    //     });
    // })

    academic_training.forEach(element => {
        element.addEventListener("mouseenter", () => { // when mouse enter the container of academic_trainings show the .see-more
            const width = window.matchMedia('(min-width: 768px)').matches
            if(width){
                collapse_all_see_more()
                see_more = element.querySelector('.see-more').classList.add('active')
                // see_more.style.right = see_more.innerHTML === 'Ver menos' ? visible - 15 + 'px' : visible + 'px'
            }
        })
        
        element.closest('.section').addEventListener("mouseleave", () => { // when mouse leave the container of academic_trainings collapse the .see-more
            const width = window.matchMedia('(min-width: 768px)').matches
            if(width){
                collapse_all_see_more()
            }
        })
        element.querySelector('.see-more').addEventListener("click", () => { // when click in .see-more element
            toggle_width(element)
        })
    });

}

function toggle_width(element) {
    information_container = element.parentNode.querySelector('.information-container') // get the parent element and search for the .resume-information-container between your childs
    about_container = information_container.querySelector('.about-container')
    if(about_container.classList.contains('active')) {
        about_container.style.opacity = '0'
        about_container.classList.remove('active')

    } else {
        collapse_all()
        setTimeout(() => {        
            about_container.classList.add('active')
        }, 200);
        setTimeout(() => {
            about_container.style.opacity = '1'
        }, 400);
    }
}
function collapse_height() {

}
function collapse_all() {
    about_container_list = document.querySelectorAll('.about-container')
    about_container_list.forEach(element => {
        element.style.opacity = '0'
        setTimeout(() => {
            element.classList.remove('active')
        }, 100);

        see_more_list = document.querySelectorAll('.see-more')
        see_more_list.forEach(element => {
            element.classList.remove('active')
            element.innerHTML = 'Ver mais'
        })
    })
}
function collapse_all_see_more() {
    see_more_list = document.querySelectorAll('.see-more')
    see_more_list.forEach(element => {
        element.classList.remove('active')
    })
}
