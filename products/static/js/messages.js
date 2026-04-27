setTimeout(() => {
  const messages = document.querySelectorAll(".my-message");

  messages.forEach(msg => {
    msg.remove();
  });

}, 10000);