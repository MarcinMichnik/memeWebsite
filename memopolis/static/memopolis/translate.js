function translate() {
    const title = document.querySelector('label.requiredField');

    if (title.innerText=='Title*') {
        title.innerText = 'Tytuł*';
    }
    
    if (title.innerText=='Content*'){
        title.innerText = 'Tekst*';
    }
    const img = document.querySelectorAll('label.requiredField')[4];
    img.innerText = 'Obrazek*';
}
