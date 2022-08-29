let input = document.querySelector('.input')
let show = document.querySelector('.show')

show.addEventListener('click', ()=>{
    show.classList.toggle('hide')
    if(input.type === 'password'){
        input.type = 'type';
    }
    else{
        input.type = 'password';
    }
})