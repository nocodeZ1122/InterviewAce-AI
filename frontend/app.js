// ======================================================
// InterviewAce AI
// Frontend Application
// Version 2
// ======================================================

const App = {

    // ==================================================
    // CONFIGURATION
    // ==================================================

    config: {

        apiBase: "http://localhost:8000",

        endpoints: {

            questions: "/questions/",
            chat: "/chat",
            review: "/review"

        }

    },



    // ==================================================
    // APPLICATION STATE
    // ==================================================

    state: {

        currentQuestion: null,

        currentMode: "explain",

        isLoading: false,

        language: "cpp"

    },



    // ==================================================
    // DOM REFERENCES
    // ==================================================

    elements: {},



    // ==================================================
    // INITIALIZATION
    // ==================================================

    init() {

        this.cacheElements();

        this.attachEventListeners();

        this.loadQuestions();

    },



    // ==================================================
    // CACHE DOM REFERENCES
    // ==================================================

    cacheElements() {

        this.elements = {

            listView:
                document.getElementById("list-view"),

            chatView:
                document.getElementById("chat-view"),

            questionList:
                document.getElementById("question-list"),

            chatMessages:
                document.getElementById("chat-messages"),

            questionTitle:
                document.getElementById("chat-question-title"),

            chatForm:
                document.getElementById("chat-form"),

            chatInput:
                document.getElementById("chat-input"),

            backButton:
                document.getElementById("back-btn"),

            codeInput:
                document.getElementById("code-input"),

            modeButtons: {

                explain:
                    document.getElementById("explain-btn"),

                hint:
                    document.getElementById("hint-btn"),

                dryRun:
                    document.getElementById("dry-run-btn"),

                review:
                    document.getElementById("review-btn")

            }

        };

    },



    // ==================================================
    // EVENT LISTENERS
    // ==================================================

    attachEventListeners() {

        this.elements.backButton.addEventListener(

            "click",

            () => this.showQuestionList()

        );

        this.elements.chatForm.addEventListener(

            "submit",

            (event) => {

                event.preventDefault();

                this.sendMessage();

            }

        );

        this.elements.chatInput.addEventListener(

            "keydown",

            (event) => {

                if (event.key === "Enter" && !event.shiftKey) {

                    event.preventDefault();

                    this.sendMessage();

                }

            }

        );

        this.elements.modeButtons.explain.addEventListener(

            "click",

            () => this.setMode("explain")

        );

        this.elements.modeButtons.hint.addEventListener(

            "click",

            () => this.setMode("hint")

        );

        this.elements.modeButtons.dryRun.addEventListener(

            "click",

            () => this.setMode("dry_run")

        );

        this.elements.modeButtons.review.addEventListener(

            "click",

            () => this.setMode("review")

        );

    }, 
        // ==================================================
    // API HELPERS
    // ==================================================

    getUrl(endpoint) {

        return this.config.apiBase + endpoint;

    },



    async apiRequest(endpoint, options = {}) {

        try {

            const response = await fetch(
                this.getUrl(endpoint),
                options
            );

            if (!response.ok) {

                throw new Error(
                    `Server responded with ${response.status}`
                );

            }

            return await response.json();

        }

        catch (error) {

            console.error(error);

            throw error;

        }

    },



    // ==================================================
    // VIEW SWITCHING
    // ==================================================

    showQuestionList() {

        this.elements.listView.classList.remove("hidden");

        this.elements.chatView.classList.add("hidden");

    },



    showChatView() {

        this.elements.listView.classList.add("hidden");

        this.elements.chatView.classList.remove("hidden");

    },



    // ==================================================
    // LOADING STATE
    // ==================================================

    setLoading(isLoading) {

        this.state.isLoading = isLoading;

        const sendButton =
            this.elements.chatForm.querySelector("button");

        sendButton.disabled = isLoading;

        Object.values(this.elements.modeButtons)
            .forEach(button => {

                button.disabled = isLoading;

            });

    },



    // ==================================================
    // LOAD QUESTIONS
    // ==================================================

    async loadQuestions() {

        this.elements.questionList.innerHTML =
            `<p class="loading-text">Loading questions...</p>`;

        try {

            const questions =
                await this.apiRequest(
                    this.config.endpoints.questions
                );

            this.renderQuestionList(questions);

        }

        catch (error) {

            this.elements.questionList.innerHTML = `

                <p class="error-text">

                    Failed to load questions.

                    <br><br>

                    ${error.message}

                </p>

            `;

        }

    },



    // ==================================================
    // RENDER QUESTION LIST
    // ==================================================

    renderQuestionList(questions) {

        if (!questions.length) {

            this.elements.questionList.innerHTML =

                `<p class="loading-text">

                    No questions available.

                </p>`;

            return;

        }

        this.elements.questionList.innerHTML =
            questions.map(question => `

            <div
                class="question-card"
                data-id="${question.id}"
            >

                <div class="question-card-top">

                    <span class="question-title">

                        ${this.escapeHtml(question.title)}

                    </span>

                    <span
                        class="tag tag-${question.difficulty.toLowerCase()}"
                    >

                        ${question.difficulty}

                    </span>

                </div>

                <div class="question-topic">

                    ${this.escapeHtml(question.topic)}

                </div>

            </div>

        `).join("");



        document
            .querySelectorAll(".question-card")
            .forEach(card => {

                card.addEventListener("click", () => {

                    const question =
                        questions.find(
                            q => q.id == card.dataset.id
                        );

                    this.openQuestion(question);

                });

            });

    },
        // ==================================================
    // OPEN QUESTION
    // ==================================================

    openQuestion(question) {

        this.state.currentQuestion = question;

        this.state.currentMode = "explain";

        this.elements.questionTitle.textContent = question.title;

        this.elements.chatMessages.innerHTML = "";

        this.elements.chatInput.value = "";

        this.elements.codeInput.value = "";

        this.setMode("explain");

        this.addMessage(
            "ai",
            `# ${question.title}

Welcome! I'm your AI interviewer.

I can help you with:

- 💬 Explain the problem
- 💡 Give hints
- ▶️ Dry run examples
- 📝 Review your code

Try solving the problem first, then ask whenever you're stuck.`
        );

        this.showChatView();

        this.elements.chatInput.focus();

    },



    // ==================================================
    // MODE SWITCHING
    // ==================================================

    setMode(mode) {

        this.state.currentMode = mode;

        Object.values(this.elements.modeButtons)
            .forEach(button =>
                button.classList.remove("active")
            );

        this.elements.codeInput.classList.add("hidden");

        switch (mode) {

            case "explain":

                this.elements.modeButtons.explain
                    .classList.add("active");

                break;

            case "hint":

                this.elements.modeButtons.hint
                    .classList.add("active");

                break;

            case "dry_run":

                this.elements.modeButtons.dryRun
                    .classList.add("active");

                break;

            case "review":

                this.elements.modeButtons.review
                    .classList.add("active");

                this.elements.codeInput
                    .classList.remove("hidden");

                break;

        }

    },



    // ==================================================
    // MESSAGE RENDERING
    // ==================================================

    addMessage(sender, content) {

        const bubble = document.createElement("div");

        bubble.classList.add(
            "msg",
            sender === "user"
                ? "msg-user"
                : "msg-ai"
        );

        if (sender === "user") {

            bubble.textContent = content;

        }

        else {

            bubble.innerHTML = marked.parse(content);

            bubble
                .querySelectorAll("pre code")
                .forEach(block => {

                    hljs.highlightElement(block);

                });

        }

        this.elements.chatMessages.appendChild(bubble);

        this.scrollToBottom();

        return bubble;

    },



    // ==================================================
    // LOADING MESSAGE
    // ==================================================

    createLoadingBubble() {

        const bubble =
            this.addMessage(
                "ai",
                "_Thinking..._"
            );

        bubble.classList.add("msg-loading");

        return bubble;

    },



    // ==================================================
    // UPDATE AI RESPONSE
    // ==================================================

    updateAIBubble(bubble, markdown) {

        bubble.innerHTML = marked.parse(markdown);

        bubble.classList.remove("msg-loading");

        bubble
            .querySelectorAll("pre code")
            .forEach(block => {

                hljs.highlightElement(block);

            });

        this.scrollToBottom();

    },



    // ==================================================
    // AUTO SCROLL
    // ==================================================

    scrollToBottom() {

        this.elements.chatMessages.scrollTo({

            top:
                this.elements.chatMessages.scrollHeight,

            behavior: "smooth"

        });

    },
        // ==================================================
    // SEND MESSAGE
    // ==================================================

    async sendMessage() {

        if (this.state.isLoading) return;

        if (!this.state.currentQuestion) return;

        const message = this.elements.chatInput.value.trim();

        if (
            this.state.currentMode !== "review" &&
            !message
        ) {
            return;
        }

        if (
            this.state.currentMode === "review" &&
            !this.elements.codeInput.value.trim()
        ) {

            alert("Please paste your solution first.");

            return;

        }

        if (message) {

            this.addMessage("user", message);

        }

        this.elements.chatInput.value = "";

        const loadingBubble =
            this.createLoadingBubble();

        this.setLoading(true);

        try {

            const response =
                   await this.requestTutor(message);

            this.updateAIBubble(
                loadingBubble,
                response
            );

            if (
                this.state.currentMode === "review"
            ) {

                this.elements.codeInput.value = "";

            }

        }

        catch (error) {

            this.showError(
                loadingBubble,
                error
            );

        }

        finally {

            this.setLoading(false);

        }

    },



    // ==================================================
    // REQUEST TUTOR
    // ==================================================

    async requestTutor(message) {

        if (
            this.state.currentMode === "review"
        ) {

            return await this.requestReview(message);

        }

        return await this.requestChat(message);

    },



    // ==================================================
    // CHAT REQUEST
    // ==================================================

    async requestChat(message) {

        const payload = {

            question_id:
                this.state.currentQuestion.id,

            message: message ,
                

            mode:
                this.state.currentMode

        };

        const data =
            await this.apiRequest(

                this.config.endpoints.chat,

                {

                    method: "POST",

                    headers: {

                        "Content-Type":
                            "application/json"

                    },

                    body:
                        JSON.stringify(payload)

                }

            );

        return data.reply;

    },



    // ==================================================
    // REVIEW REQUEST
    // ==================================================

    async requestReview() {

        const payload = {

            question_id:
                this.state.currentQuestion.id,

            language:
                this.state.language,

            code:
                this.elements.codeInput.value

        };

        const data =
            await this.apiRequest(

                this.config.endpoints.review,

                {

                    method: "POST",

                    headers: {

                        "Content-Type":
                            "application/json"

                    },

                    body:
                        JSON.stringify(payload)

                }

            );

        return data.review;

    },



    // ==================================================
    // ERROR HANDLING
    // ==================================================

    showError(
        bubble,
        error
    ) {

        let message =
            "Something went wrong.";

        if (
            error.message.includes("Failed to fetch")
        ) {

            message =

`## Unable to reach the backend

Make sure:

- FastAPI is running
- The server is on localhost:8000
- CORS is enabled`;

        }

        else {

            message =

`## Error

${error.message}`;

        }

        bubble.innerHTML =
            marked.parse(message);

        bubble.classList.remove(
            "msg-loading"
        );

    },
        // ==================================================
    // ESCAPE HTML
    // ==================================================

    escapeHtml(text) {

        if (text === null || text === undefined) {

            return "";

        }

        const div =
            document.createElement("div");

        div.textContent = text;

        return div.innerHTML;

    },



    // ==================================================
    // RESET CHAT
    // ==================================================

    resetChat() {

        this.elements.chatMessages.innerHTML = "";

        this.elements.chatInput.value = "";

        this.elements.codeInput.value = "";

        this.setMode("explain");

    },



    // ==================================================
    // RESET MODES
    // ==================================================

    resetModes() {

        Object
            .values(this.elements.modeButtons)
            .forEach(button => {

                button.classList.remove("active");

            });

    },



    // ==================================================
    // SHOW NOTIFICATION
    // ==================================================

    notify(message) {

        console.log("[InterviewAce]", message);

    },



    // ==================================================
    // APPLICATION START
    // ==================================================

    start() {

        this.init();

        this.notify("Application Started.");

    }

};


// ======================================================
// START APPLICATION
// ======================================================

document.addEventListener(

    "DOMContentLoaded",

    () => {

        App.start();

    }

);



// ======================================================
// GLOBAL ERROR HANDLING
// ======================================================

window.addEventListener(

    "error",

    (event) => {

        console.error(event.error);

    }

);

window.addEventListener(

    "unhandledrejection",

    (event) => {

        console.error(event.reason);

    }

);