document.getElementById("ask-help").addEventListener("click", () => {
    document.getElementById("chat-box").style.display = "block";
  });
  
  document.getElementById("submit-question").addEventListener("click", () => {
    const userQuestion = document.getElementById("user-question").value;
    if (userQuestion) {
      addMessageToChat('user', userQuestion); // Add user message to chat before getting AI answer
      getAnswerFromAI(userQuestion);
      document.getElementById("user-question").value = ''; // Clear the textarea after submission
    }
  });
  
  async function getAnswerFromAI(question) {
    try {
        const response = await fetch('http://localhost:5000/get_answer', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ question })
        });
        const data = await response.json();
        addMessageToChat('assistant', data.answer); //add the assistant response
    } catch (error) {
        addMessageToChat('assistant', "Sorry, I couldn't fetch the answer.");
    }
  }

  function addMessageToChat(sender, message) {
    const chatBox = document.getElementById("response");
    const messageDiv = document.createElement("div");
    messageDiv.classList.add('chat-message');
    messageDiv.classList.add(sender);

    messageDiv.textContent = message;
    chatBox.appendChild(messageDiv);

    chatBox.scrollTop = chatBox.scrollHeight; // Keep scroll at bottom
    saveChatHistory();
}
  
  function saveChatHistory() {
    const chatBox = document.getElementById("response");
    const chatHistory = chatBox.innerHTML;
    chrome.storage.local.set({ chatHistory: chatHistory });
  }
  
  function loadChatHistory() {
    chrome.storage.local.get(["chatHistory"], (result) => {
        const chatBox = document.getElementById("response");
      if (result.chatHistory) {
        chatBox.innerHTML = result.chatHistory;
      }
       chatBox.scrollTop = chatBox.scrollHeight;
    });
  }
  
  loadChatHistory(); // Load chat history on popup load