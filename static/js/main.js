let cenres_link = document.getElementById('cenres_link')
let cenres = document.getElementById('cenres')

cenres_link.addEventListener('mouseover', e =>{
    cenres.classList.remove('d-none')
})

cenres_link.addEventListener('mouseout', e =>{
    cenres.classList.add('d-none')
})