# Web application for Therapist:

A web application for a neurotherapist and hypnotherapist specialised in emotional detachment, the management of negative emotions, and the healing of traumas and wounds.

## Team
- Name: Anthony COINTRE
- Role: Website Developer
- Justification: I am responsible for all aspects of development, design, and deployment.

## Technologies
- Libraries:
    - Calendly for embedding scheduling functionality via the calendly-inline-widget.
    - json for handling reading from and writing to JSON files (for user data in this case).
    - bcrypt for securely hashing and checking passwords.
    - Jinja2 for rendering HTML templates dynamically.

- Languages:
    - HTML/CSS for structuring and styling web pages.
    - JavaScript for adding dynamic and interactive functionality to web pages.
    - Python for backend development and logic implementation.

- Platforms:
    - GitHub for source code management.

- Frameworks:
    - Flask for building web applications in Python with flexibility and minimal overhead.

- Hardware:
    - Personal computers for web application development and management.
- Books:
    -
- Resources:
    - Stack Overflow for solving common development problems.
GitHub for similar open source projects.

- Technology Trade-offs:
    - Calendly offers a complete scheduling solution with booking, reminders, and calendar integrations, while FullCalendar.js is a customizable calendar interface, but lacks built-in scheduling and appointment management features.
    - SQL databases like MySQL offer robust relational data handling and consistency, but they can be less flexible in terms of schema changes and scaling horizontally compared to NoSQL databases, which are more adaptable and scalable but may sacrifice some data consistency and complex querying capabilities.

## Challenge
- Problem Statement: The Portfolio project allows a therapist to have her own website that manages appointment bookings.
- What the Project Will Not Solve: The project doesn’t allow for a videoconference session directly on the website, there is a link to another application.
- Target Users: The project helps patients in need of therapy.
- Locale Relevance: The project is designed for French users.

## Risks
- Technical Risks:
    - Risk: Security vulnerabilities during data transmission (name and first name used in the username).
    - Potential Impact: Data breaches could compromise client privacy.
    - Safeguards:
- Non-Technical Risks:
    - Risk: Non-compliance with laws and regulations (e.g., GDPR, CCPA).
    - Potential Impact: Fines, legal action, reputation damage.
    - Strategy: Stay informed about relevant laws, consult legal experts, and implement clear privacy policies and terms of service.

## Infrastructure
- Branching and Merging:
    - I will use GitHub to manage the repository, where all development occurs on feature branches off the ‘main’ branch. Once a feature is complete and tested, I'll create a Pull Request for code review. After passing automated tests and resolving any conflicts, I will merge the feature into ‘main’ using squash merging to keep the commit history clean.
- Deployment Strategy:
    - For deployment, I will only deposit my files on GitHub.
- Data Population:
    - I will populate the application with fictitious data such as “testuser” or “anthony” as users and use simple passwords.
- Testing:
    - My testing strategy includes manual testing for the Login and Sign Up.

## Existing Solutions
- Similar Products:
    - Calendly
        - Similarities:
            - Calendly allows users to book available time slots online, which is similar to what you’re looking at.
            - You can set available time slots for phone calls, just like Calendly.
        - Differences:
            - Calendly offers a variety of appointment types and lets you customise durations and rules for each type, which can be more flexible than your site if you have a variety of needs.
            - Calendly offers integrations with calendars like Google Calendar and Outlook to avoid double bookings, which may not be necessary for a phone booking site if you don’t need to sync with external calendars.
    - Doctolib
        - Similarities:
            - Doctolib allows users to book appointments online for phone calls.
        - Differences:
            - Doctolib is primarily aimed at healthcare professionals, with tailored features (medical records, teleconsultations), which are unlikely to be necessary for a phone appointment booking service.
            - Doctolib includes medical records and consultation management features, which is more complex than what you need for initial phone consultations.
    - Crenolibre
        - Similarities:
            - Crenolibre allows online booking of time slots for different services.
        - Differences:
            - Crenolibre also offers management of physical space bookings, which is not relevant for a phone appointment booking site.
            - Crenolibre can be used for various services and spaces, while your site focuses specifically on phone calls for session decisions.
    - Therapeutes.com
        - Similarities:
            - Therapeutes.com allows users to book time slots to chat with a professional.
        - Differences:
            - Therapeutes.com is focused on booking appointments with therapists, with detailed profiles and options specific to therapy services. Your site focuses on booking phone calls to schedule sessions, which may not require as much detail or specialisation.
            - Therapeutes.com offers comprehensive therapist profiles, including reviews and detailed information, while your site may be simpler, with a booking feature focused solely on phone calls.
