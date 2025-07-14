window.onload = function(){
    
    academic_training = document.querySelectorAll(".list-item")
    collapsed = -10
    visible =  -80


    // verify if is desktop or mobile and manipulate the position of .see-more elements
    window.matchMedia('(max-width: 768px)').addEventListener('change', () => { 
        see_more = document.querySelectorAll('.see-more')
        see_more.forEach(element => {
            if(window.matchMedia('(max-width: 768px)').matches){
                element.style.right = ''
            } else {
                element.style.right = collapsed + 'px'
            }
        });
    })  
    window.matchMedia('(min-width: 768px)').addEventListener('change', () => { 
        see_more = document.querySelectorAll('.see-more')
        see_more.forEach(element => {
            if(window.matchMedia('(max-width: 768px)').matches){
                element.style.right = ''
            } else {
                element.style.right = collapsed + 'px'
            }
        });
    })

    academic_training.forEach(element => {
        element.addEventListener("mouseenter", () => { // when mouse enter the container of academic_trainings show the .see-more
            const width = window.matchMedia('(min-width: 768px)').matches
            if(width){
                see_more_list = document.querySelectorAll('.see-more')
                see_more_list.forEach(element => {
                    element.style.right = collapsed + 'px'
                })
                see_more = element.querySelector('.see-more')
                see_more.style.right = see_more.innerHTML === 'Ver menos' ? visible - 15 + 'px' : visible + 'px'
            }
        })
        element.closest('.section').addEventListener("mouseleave", () => { // when mouse leave the container of academic_trainings collapse the .see-more
            const width = window.matchMedia('(min-width: 768px)').matches
            if(width){
                see_more_list = element.querySelectorAll('.see-more')
                see_more_list.forEach(element => {
                    element.style.right =  collapsed + 'px'
                })
            }
        })
        element.querySelector('.see-more').addEventListener("click", () => { // when click in .see-more element
            information_container = element.parentNode.querySelector('.information-container') // get the parent element and search for the .resume-information-container between your childs
            if ('0px'.includes(information_container.querySelector('.about-container').style.maxHeight)){ // verify if exists .see-more in the information_container
                about_container_list = document.querySelectorAll('.about-container')
                about_container_list.forEach(element => {
                    element.style.opacity = '0'
                    see_more_list = document.querySelectorAll('.see-more')
                    see_more_list.forEach(element => {
                        element.innerHTML = 'Ver mais'
                    })
                    setTimeout(() =>{
                        element.style.maxHeight = '0px'
                        element.style.maxWidth = '0px'
                    },50)
                })
                setTimeout(() => {
                    information_container.querySelector('.about-container').style.maxHeight = '400px' // add see more element
                    information_container.querySelector('.about-container').style.maxWidth = '1000px' // add see more element
                    setTimeout(() =>{
                        information_container.querySelector('.about-container').style.opacity = '1' // add see more element
                    },500)
    
                    see_more = element.querySelector('.see-more')
                    see_more.style.right = visible - 15 + 'px'
                    see_more.innerHTML = 'Ver menos' // change the text of see-more\
                }, 50)
            } else {
                information_container.querySelector('.about-container').style.opacity = '0' // remove the see-more element
                setTimeout(() =>{
                    information_container.querySelector('.about-container').style.maxHeight = '0px' // remove the see-more element
                    information_container.querySelector('.about-container').style.maxWidth = '0px' // remove the see-more element
                },50)
                see_more = element.querySelector('.see-more')
                see_more.innerHTML = 'Ver mais' // change the text of see-more
            }
        })
        
    });
    
}
