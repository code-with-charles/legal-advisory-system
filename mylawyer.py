import customtkinter as ctk
from pyknow import *

# Legal knowledge base using PyKnow
class LegalAdvisory(KnowledgeEngine):
    # Define rules for Employment Law
    @Rule(Fact(topic="employment_law"), Fact(question="fired"))
    def employment_rights(self):
        self.declare(Fact(response="If you are fired, you may have rights to severance pay, unemployment benefits, and possibly a wrongful termination claim. It's crucial to understand the specific terms outlined in your employment contract, as different states may have varying regulations. Consulting local laws is essential to ascertain your entitlements."))

    @Rule(Fact(topic="employment_law"), Fact(question="cut"))
    def pay_cut_rights(self):
        self.declare(Fact(response="An employer generally cannot reduce your pay without your consent. If a pay cut is not stipulated in your employment contract or if you weren't informed in advance, you may have grounds to contest this action. It is advisable to engage in a discussion with your HR department if you believe your contract is being violated."))

    @Rule(Fact(topic="employment_law"), Fact(question="harassed"))
    def harassment_rights(self):
        self.declare(Fact(response="If you're being harassed in the workplace, it's critically important to take immediate action. Document all incidents thoroughly, noting dates, times, and any witnesses who may support your claims. Reporting the situation to your Human Resources department is a necessary step, as they are required to investigate any claims of harassment."))

    # Define rules for Family Law
    @Rule(Fact(topic="family_law"), Fact(question="divorce"))
    def divorce_rights(self):
        self.declare(Fact(response="In the event of a divorce, you may have rights to alimony, child support, and a fair division of marital property. These rights can depend on factors such as the duration of the marriage and the financial circumstances of both parties. Therefore, it is highly advisable to seek counsel from a family law attorney who can guide you through the process."))

    @Rule(Fact(topic="family_law"), Fact(question="child custody"))
    def child_custody(self):
        self.declare(Fact(response="Child custody is primarily determined based on what is in the best interest of the child. This evaluation includes various factors such as the child’s age, emotional ties to each parent, and the overall home environment. Courts prioritize the child's welfare, which is the cornerstone of any custody arrangement."))

    @Rule(Fact(topic="family_law"), Fact(question="parent"))
    def parental_rights(self):
        self.declare(Fact(response="As a parent, you generally possess rights to custody, visitation, and significant decision-making regarding your child's education and health. Understanding these rights is essential for effectively navigating custody arrangements during separation or divorce, as these rights can greatly impact your ongoing relationship with your child."))

    # Define rules for General questions
    @Rule(Fact(topic="general"), Fact(question="ticket"))
    def traffic_ticket(self):
        self.declare(Fact(response="If you receive a traffic ticket, you have several options available to you. These options generally include paying the fine, contesting the ticket in court, or, in some cases, attending traffic school to reduce penalties. It’s advisable to gather any evidence and understand your local traffic laws if you choose to contest the ticket."))

    @Rule(Fact(topic="general"), Fact(question="will"))
    def create_will(self):
        self.declare(Fact(response="Creating a will is an essential step in planning how your assets will be distributed after your passing. It involves outlining your wishes for asset distribution and appointing guardians for any dependents. Consulting with an attorney who specializes in estate planning is highly advisable to ensure that your will adheres to the legal requirements of your state."))

    @Rule(Fact(topic="general"), Fact(question="power of attorney"))
    def power_of_attorney(self):
        self.declare(Fact(response="A power of attorney (POA) allows you to designate someone to make decisions on your behalf if you become unable to do so due to illness or incapacity. It can be tailored as a durable POA, which remains effective even if you're incapacitated, or as a non-durable POA that is only effective during a specified time period."))

    @Rule(Fact(topic="general"), Fact(question="tenant"))
    def tenant_rights(self):
        self.declare(Fact(response="As a tenant, you have rights that protect you from unfair rental practices. These rights generally include the right to a habitable living environment, protection against eviction without appropriate notice, and the right to privacy from your landlord. Familiarizing yourself with local landlord-tenant laws is essential for understanding your rights and obligations."))

    @Rule(Fact(topic="general"), Fact(question="employment rights"))
    def employment_rights_general(self):
        self.declare(Fact(response="Employment rights encompass a variety of protections for workers, including the right to fair wages, safe working conditions, and freedom from discrimination in the workplace. Understanding your rights according to local labor laws is crucial, especially if you face issues such as harassment, unjust termination, or unsafe work environments."))

# Main GUI Application
class LegalAdvisoryApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Legal Advisory System")
        self.geometry("800x600")
        self.configure(fg_color="#2C2F33")

        # Initialize the legal engine
        self.engine = LegalAdvisory()
        self.engine.reset()

        # Set up the UI layout
        self.setup_ui()

    def setup_ui(self):
        # Title Label
        self.title_label = ctk.CTkLabel(self, text="Legal Advisory System", font=("Arial", 24), text_color="white")
        self.title_label.pack(pady=20)

        # Dropdown for selecting legal category
        self.category_label = ctk.CTkLabel(self, text="Select Legal Category:", font=("Arial", 18), text_color="white")
        self.category_label.pack()
        self.category_dropdown = ctk.CTkComboBox(self, values=["Employment Law", "Family Law", "General"])
        self.category_dropdown.pack(pady=10)

        # Input field for typing legal questions
        self.input_label = ctk.CTkLabel(self, text="Enter your legal question:", font=("Arial", 18), text_color="white")
        self.input_label.pack()
        self.input_box = ctk.CTkEntry(self, width=600, height=40, font=("Arial", 16))
        self.input_box.pack(pady=10)

        # Button to submit the query
        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.process_query)
        self.submit_button.pack(pady=20)

        # Text area to display responses
        self.response_area = ctk.CTkTextbox(self, width=600, height=200, font=("Arial", 16))
        self.response_area.pack(pady=20)

        # Example Questions Section
        self.example_label = ctk.CTkLabel(self, text="Example Questions:", font=("Arial", 18), text_color="white")
        self.example_label.pack(pady=10)
        self.example_text = ctk.CTkTextbox(self, width=600, height=100, font=("Arial", 14), state="disabled")
        self.example_text.pack(pady=10)
        self.example_text.configure(state="normal")
        self.example_text.insert("1.0",
            "1. What are my rights if I am fired?\n"
            "2. Can my employer cut my pay?\n"
            "3. What should I do if I am harassed at work?\n"
            "4. What are my rights in a divorce?\n"
            "5. How is child custody determined?\n"
            "6. What rights do I have as a parent?\n"
            "7. What should I do if I get a traffic ticket?\n"
            "8. How do I create a will?\n"
            "9. What is a power of attorney?\n"
            "10. What are my tenant rights?\n"
            "11. What are my employment rights?\n"
        )
        self.example_text.configure(state="disabled")

    def process_query(self):
        category = self.category_dropdown.get().strip().lower().replace(" ", "_")
        question = self.input_box.get().strip().lower()  # Normalize question to lower case

        # Clear previous response
        self.response_area.delete("1.0", ctk.END)

        # Check if a valid category is selected
        if category not in ["employment_law", "family_law", "general"]:
            self.response_area.insert("1.0", "Please select a valid legal category.\n")
            return

        # Declare the topic in the engine
        self.engine.declare(Fact(topic=category))

        # Check for keywords based on user input
        self.evaluate_keywords(question)

        # Run the engine
        self.engine.run()

        # Display response
        self.display_rule_based_response()

    def evaluate_keywords(self, question):
        keywords = {
            "employment_law": ["fired", "cut", "harassed"],
            "family_law": ["divorce", "child custody", "parent"],
            "general": ["ticket", "will", "power of attorney", "tenant", "employment"]
        }

        # Check if the question contains any of the keywords
        for keyword in keywords[self.category_dropdown.get().strip().lower().replace(" ", "_")]:
            if keyword in question:
                self.engine.declare(Fact(question=keyword))  # Declare the keyword fact
                return  # Exit after the first match

    def display_rule_based_response(self):
        response_found = False
        for fact in self.engine.facts.values():
            if isinstance(fact, Fact) and 'response' in fact:
                response_text = fact['response']
                self.response_area.insert("1.0", response_text + "\n")
                response_found = True
                break

        if not response_found:
            self.response_area.insert("1.0", "No response available for this question.\n")

        self.engine.reset()  # Reset the engine for the next query

if __name__ == "__main__":
    app = LegalAdvisoryApp()
    app.mainloop()
