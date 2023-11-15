document.addEventListener('DOMContentLoaded', function () {


    var form = document.querySelector(".form");
    var trigger = document.querySelector(".trigger");
    var closeButton = document.querySelector(".close-button");

    function toggleModal() {
        form.classList.toggle("show-form");
    }

    function windowOnClick(event) {
        if (event.target === form) {
            toggleModal();
        }
    }

    trigger.addEventListener("click", toggleModal);
    closeButton.addEventListener("click", toggleModal);
    window.addEventListener("click", windowOnClick);

});

