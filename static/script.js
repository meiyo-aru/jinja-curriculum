window.onload = function(){
    
    li_card = document.querySelectorAll("li.card")

    // // verify if is desktop or mobile and manipulate the position of #see-more span elements
    // window.matchMedia('(max-width: 768px)').addEventListener('change', () => { 
    //     see_more = document.querySelectorAll('#see-more span')
    //     see_more.forEach(element => {
    //         if(window.matchMedia('(max-width: 768px)').matches){
    //             element.style.right = ''
    //         } else {
    //             element.style.right = collapsed + 'px'
    //         }
    //     });
    // })  
    // window.matchMedia('(min-width: 768px)').addEventListener('change', () => { 
    //     see_more = document.querySelectorAll('#see-more span')
    //     see_more.forEach(element => {
    //         if(window.matchMedia('(max-width: 768px)').matches){
    //             element.style.right = ''
    //         } else {
    //             element.style.right = collapsed + 'px'
    //         }
    //     });
    // })

    li_card.forEach(element => {
        element.addEventListener("mouseenter", () => { // when mouse enter the container of li_cards show the #see-more span
            const width = window.matchMedia('(min-width: 768px)').matches
            if(width){
                collapse_all_see_more()
                element.querySelector('#see-more span').classList.add('active')
            }
        })
        
        element.closest('section.card').addEventListener("mouseleave", () => { // when mouse leave the container of li_cards collapse the #see-more span
            const width = window.matchMedia('(min-width: 768px)').matches
            if(width){
                collapse_all_see_more()
            }
        })
        element.querySelector('#see-more span').addEventListener("click", () => { // when click in #see-more span element
            toggle_width(element)
        })
    });

}

function toggle_width(element) {
    about_container = element.closest('.card').querySelector('.expansive-container')
    if(about_container.classList.contains('active')) {
        about_container.style.opacity = '0'
        about_container.classList.remove('active')
        see_more = element.querySelector('#see-more span')
        see_more.innerHTML = 'Ver mais'
        see_more.classList.remove('active-clicked')
    } else {
        collapse_all()
        setTimeout(() => {        
            about_container.classList.add('active')
            see_more = element.querySelector('#see-more span')
            see_more.innerHTML = 'Ver menos'
            see_more.classList.add('active-clicked')
        }, 200);
        setTimeout(() => {
            about_container.style.opacity = '1'
        }, 400);
    }
}

function collapse_all() {
    about_container_list = document.querySelectorAll('.expansive-container')
    about_container_list.forEach(element => {
        element.style.opacity = '0'
        setTimeout(() => {
            element.classList.remove('active')
        }, 100);
    })
}
function collapse_all_see_more() {
    see_more_list = document.querySelectorAll('#see-more span')
    see_more_list.forEach(element => {
        element.classList.remove('active')
    })
}
