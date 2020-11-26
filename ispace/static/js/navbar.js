document.getElementById('mobile-navbar-button').addEventListener('click', function () {
    let navbar = document.getElementById('mobile-navbar')
    if (navbar.classList.contains('hidden')) {
        navbar.classList.remove('hidden')
        document.getElementById('mobile-navbar-closed').classList.replace('block', 'hidden')
        document.getElementById('mobile-navbar-open').classList.replace('hidden', 'block')
    } else {
        navbar.classList.add('hidden')
        document.getElementById('mobile-navbar-closed').classList.replace('hidden', 'block')
        document.getElementById('mobile-navbar-open').classList.replace('block', 'hidden')
    }
})

// document.getElementById('user-menu').addEventListener('click', function () {
//     let dropdown = document.getElementById('user-menu-dropdown')
//     if (dropdown.classList.contains('hidden')) {
//         dropdown.classList.replace('hidden')
//     } else {
//         dropdown.classList.add('hidden')
//     }
// })
