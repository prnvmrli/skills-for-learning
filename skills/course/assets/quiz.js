// Reusable multiple-choice quiz.
// Markup: <ol class="quiz"><li data-answer="N"><p>Question</p><button>..</button>…<p class="why">..</p></li></ol>
// N is the 0-based index of the correct button. One attempt per question; feedback is immediate.
document.querySelectorAll('ol.quiz').forEach((quiz) => {
  const items = [...quiz.children];
  const score = document.createElement('p');
  score.className = 'score';
  score.setAttribute('aria-live', 'polite');
  quiz.after(score);
  let right = 0;
  let done = 0;
  const update = () => {
    score.textContent = `${right} of ${items.length} correct` + (done === items.length ? ' · finished' : '');
  };
  items.forEach((li) => {
    const buttons = [...li.querySelectorAll('button')];
    const answer = Number(li.dataset.answer);
    buttons.forEach((b, i) => b.addEventListener('click', () => {
      if (li.classList.contains('answered')) return;
      done++;
      if (i === answer) right++;
      b.classList.add(i === answer ? 'right' : 'wrong');
      buttons[answer].classList.add('right');
      buttons.forEach((x) => { x.disabled = true; });
      li.classList.add('answered');
      update();
    }));
  });
  update();
});
