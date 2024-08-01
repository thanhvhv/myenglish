document.addEventListener('DOMContentLoaded', () => {
    const vocabInput = document.getElementById('vocab-input');
    const feedback = document.getElementById('feedback');
    const showAnswerBtn = document.getElementById('show-answer-btn');
    const nextStepBtn = document.getElementById('next-step-btn');
    const answerDiv = document.getElementById('answer');
    const correctWordSpan = document.getElementById('correct-word');
    const correctCountSpan = document.getElementById('correct-count-span');
    const badgeContainer = document.getElementById('badge-container');
    const correctBadge = document.getElementById('correct-badge');
    const vocabContainer = document.getElementById('vocab-container');
    const wordComponents = document.querySelectorAll('.word-component');
    let currentWordIndex = 0;
    let correctWordsCount = 0;

    function updateVocabWord() {
        wordComponents.forEach((component, index) => {
            component.style.display = index === currentWordIndex ? 'block' : 'none';
        });
        const currentWordComponent = wordComponents[currentWordIndex];
        if (currentWordComponent) {
            const vocabWordSpan = currentWordComponent.querySelector('.vocab-word').textContent;
            correctWordSpan.textContent = vocabWordSpan;
            vocabInput.value = '';
            vocabInput.classList.remove('is-valid', 'is-invalid');
            feedback.classList.remove('d-block');
            showAnswerBtn.classList.remove('d-none');
            answerDiv.classList.add('d-none');
            vocabInput.focus();
        } else {
            showAnswerBtn.classList.add('d-none');
            nextStepBtn.classList.remove('d-none');
            displayBadge();
            hideInputComponents();
        }
    }

    function checkVocabulary() {
        const userInput = vocabInput.value.trim().toLowerCase();
        const currentWordComponent = wordComponents[currentWordIndex];
        const correctWord = currentWordComponent.getAttribute('data-word').toLowerCase();
        if (userInput === correctWord) {
            vocabInput.classList.remove('is-invalid');
            vocabInput.classList.add('is-valid');
            feedback.classList.remove('d-block');
            feedback.classList.add('d-none');
            correctWordsCount++;
            correctCountSpan.textContent = correctWordsCount;
            setTimeout(nextVocabulary, 1000);  // Delay for 1 second before moving to the next word
        } else {
            vocabInput.classList.remove('is-valid');
            vocabInput.classList.add('is-invalid');
            feedback.classList.remove('d-none');
            feedback.classList.add('d-block');
            answerDiv.classList.add('d-none');
        }
    }

    function showAnswer() {
        answerDiv.classList.remove('d-none');
        const currentWordComponent = wordComponents[currentWordIndex];
        const correctWord = currentWordComponent.getAttribute('data-word');
        correctWordSpan.textContent = correctWord;
    }

    function nextVocabulary() {
        currentWordIndex++;
        vocabInput.value = ''; // Clear the input field
        updateVocabWord();
    }

    function displayBadge() {
        correctBadge.textContent = `You got ${correctWordsCount} words correct!`;
        badgeContainer.classList.remove('d-none');
    }

    function hideInputComponents() {
        vocabContainer.style.display = 'none';
        showAnswerBtn.style.display = 'none';
        answerDiv.style.display = 'none';
    }

    showAnswerBtn.addEventListener('click', showAnswer);

    vocabInput.addEventListener('keyup', (event) => {
        if (event.key === 'Enter') {
            checkVocabulary();
        }
    });

    updateVocabWord(); // Initialize the first vocabulary word
});