let cenres_link = document.getElementById('cenres_link')
let cenres_card = document.getElementById('cenres_card')
let cenres = document.getElementById('cenres')

cenres_card.addEventListener('mouseover', e =>{
    cenres.classList.remove('d-none')
    console.log('ejdhgced');
})

cenres_card.addEventListener('mouseout', e =>{
    cenres.classList.add('d-none')
})