### README: **Your Friendly Email Sending Bot**

#### Overview
This is a Streamlit-based web application that acts as an **Email Sending Bot**. The bot generates structured and well-crafted email content using an LLM (Language Learning Model) and facilitates sending emails via Gmail's SMTP server. Additionally, it stores details of email interactions in an Excel sheet for future reference.

---

### Features
1. **Email Generation using AI**:
   - The bot generates professional email content based on user input prompts and context.
2. **Email Sending**:
   - Securely sends emails using Gmail's SMTP server with App Password authentication.
3. **Data Logging**:
   - Logs user inputs, generated email content, and reasoning into an Excel file for record-keeping.
4. **User-Friendly Interface**:
   - Designed with Streamlit for an interactive and intuitive user experience.

---

### Requirements
- Python 3.7+
- Gmail account with App Password enabled.
- Required libraries:
  - `streamlit`
  - `openpyxl`
  - `langchain`
  - `dotenv`
  - `transformers`
  - `smtplib`

---

### Installation and Setup
1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variables**:
   - Create a `.env` file in the root directory with the following:
     ```env
     groq_API_KEY=your_groq_api_key
     ```

4. **Enable Gmail SMTP**:
   - Go to your Google account:
     - If **2FA is enabled**, generate an **App Password** under "Security > App Passwords."
     - If **2FA is not enabled**, turn on "Less Secure App Access."

5. **Run the Application**:
   ```bash
   streamlit run <script_name>.py
   ```

---

### Usage
1. **Fill in the Form**:
   - Enter your name, sender email, password (App Password), and recipient email.
   - Type your message in the chat input box.

2. **Email Generation**:
   - The bot processes the input and generates a structured email.
   - Preview the email body in the app.

3. **Send Email**:
   - The bot sends the email via Gmail's SMTP server.

4. **Logging**:
   - Email details (prompt, reasoning, response) are saved in `prompt_responce.xlsx`.

---

### File Structure
```
.
├── main.py                 # Streamlit application entry point
├── model_llm.py            # Handles LLM-based email generation
├── email_llm.py            # Handles email sending logic
├── excel_llm.py            # Handles logging data into Excel
├── prompt_responce.xlsx    # Excel file storing logs (auto-generated)
├── requirements.txt        # List of dependencies
├── .env                    # Environment variables (API keys, etc.)
```

---

### Code Explanation
#### **1. Streamlit Frontend**
- **Main Interaction**:
  ```python
  st.title("Your Friendly Email Sending Bot")
  st.header("Please fill the details before sending mail")

  name = st.text_input(label='User Name', placeholder='John')
  sender_email = st.text_input(label="Sender Email", placeholder="abc@gmail.com")
  password = st.text_input(label='Password', placeholder='********')
  reciver_email = st.text_input(label='Reciver Email', placeholder='abc@gmail.com')

  if name and sender_email and password and reciver_email:
      prompt = st.chat_input(placeholder="Type your message here...")
      if prompt:
          ...
  ```
  Users provide the details required for email generation and sending.

#### **2. LLM Email Generation**
- **LLM Integration**:
  ```python
  llm = ChatGroq(
      api_key=api_key,
      model='deepseek-r1-distill-llama-70b',
      temperature=0.3
  )
  ```
  The `get_output()` function uses an LLM from `ChatGroq` to generate email content based on user-provided prompts.

#### **3. Email Sending**
- **SMTP Logic**:
  ```python
  def send_email_to_user(semail, password, remail, subject, body):
      with smtplib.SMTP("smtp.gmail.com", 587) as server:
          server.starttls()
          server.login(sender_email, password)
          server.sendmail(sender_email, resever_email, message.as_string())
  ```
  Emails are sent securely using Gmail's SMTP server with TLS encryption.

#### **4. Logging in Excel**
- **Excel Logging**:
  ```python
  def add_data_to_excel(user, prompt, reasoning, responce, filename='prompt_responce.xlsx'):
      ...
      sheet.append([sheet.max_row, user, str(datetime.now()), prompt, reasoning, responce])
      workbook.save(filename)
  ```
  Data from email interactions is logged into an Excel file.

---

### Notes
- Ensure the `groq_API_KEY` is valid and correctly set in the `.env` file.
- Use App Passwords for Gmail accounts with 2FA enabled.
- Replace placeholders in the code (like email IDs) with your own values for testing.

---

### Troubleshooting
- **SMTP Authentication Error**:
  - Verify your email and App Password.
  - Enable "Less Secure Apps" if not using 2FA.
  - Check if Gmail's "Display Unlock Captcha" needs activation.

- **Excel File Issues**:
  - Ensure the application has write access to the working directory.

---
