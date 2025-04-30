document.getElementById('quizForm').addEventListener('submit', function(e) {
    e.preventDefault();

    // Define correct answers with question text
    const answers = {
        q1: { correct: 'a', text: '1. What is the base spirit in a Bloody Orange Martini?' },
        q2: { correct: 'a', text: '2. What citrus fruit gives the drink its name?' },
        q3: { correct: 'a', text: '3. What is a common garnish for this cocktail?' },
        q4: { correct: 'c', text: '4. What kind of glass is usually used?' },
        q5: { correct: 'b', text: '5. Which of these is a typical additional ingredient?' }
    };

    let score = 0;
    const total = Object.keys(answers).length;
    const feedbackList = document.getElementById('feedbackList');
    feedbackList.innerHTML = '';

    for (let q in answers) {
        const selected = document.querySelector(`input[name="${q}"]:checked`);
        const { correct, text } = answers[q];

        const li = document.createElement('li');
        const userAnswerText = selected ? selected.parentElement.textContent.trim() : 'No answer selected';
        const correctAnswerText = getAnswerText(q, correct);

        if (selected && selected.value === correct) {
            score++;
            li.innerHTML = `<span class="correct">✔ Correct</span> — ${text}`;
        } else {
            li.innerHTML = `
                <div>
                    <strong class="wrong-question">${text}</strong><br>
                    Your answer: <em>${userAnswerText}</em><br>
                    Correct answer: <strong>${correctAnswerText}</strong>
                </div>
            `;
        }

        feedbackList.appendChild(li);
    }

    document.getElementById('scoreText').textContent = `You scored ${score} out of ${total}!`;
    document.getElementById('quizForm').classList.add('hidden');
    document.getElementById('resultsPage').classList.remove('hidden');
});

function getAnswerText(question, value) {
    const options = document.querySelectorAll(`input[name="${question}"]`);
    for (let opt of options) {
        if (opt.value === value) {
            return opt.parentElement.textContent.trim();
        }
    }
    return '';
}