const chatContainer = document.getElementById("chatContainer");
const userInput = document.getElementById("userInput");
const sendBtn = document.getElementById("sendBtn");

userInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !sendBtn.disabled) {
        sendMessage();
    }
});

function appendMessage(role, text) {
    const div = document.createElement("div");
    div.className = `message ${role}`;
    const bubble = document.createElement("div");
    bubble.className = "bubble";
    bubble.textContent = text;
    div.appendChild(bubble);
    chatContainer.appendChild(div);
    chatContainer.scrollTop = chatContainer.scrollHeight;
    return bubble;
}

function sendMessage() {
    const query = userInput.value.trim();
    if (!query) return;

    appendMessage("user", query);
    userInput.value = "";
    sendBtn.disabled = true;

    const bubble = appendMessage("assistant", "");
    const indicator = document.createElement("span");
    indicator.className = "typing-indicator";
    bubble.appendChild(indicator);

    const encoded = encodeURIComponent(query);
    const eventSource = new EventSource(`/chat?query=${encoded}`);
    let started = false;

    eventSource.onmessage = (event) => {
        const data = event.data;

        if (data === "[DONE]") {
            eventSource.close();
            sendBtn.disabled = false;
            userInput.focus();
            return;
        }

        if (!started) {
            bubble.textContent = "";
            started = true;
        }

        bubble.textContent += data;
        chatContainer.scrollTop = chatContainer.scrollHeight;
    };

    eventSource.onerror = () => {
        eventSource.close();
        if (!started) {
            bubble.textContent = "Connection error. Make sure Ollama is running and try again.";
        }
        sendBtn.disabled = false;
    };
}
