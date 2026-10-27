import streamlit as st
import os
import pandas as pd

st.set_page_config(
    page_title= "Horigome | Portfolio",
    page_icon="⚙️", 
    layout="wide",
)

col1, col2 = st.columns(2)

with col1:
    st.title("Horigome, Ken N.")
    st.markdown("### *BS Computer Science — 3rd Year (Section F2)*")
    st.markdown(
        "> *“Always take time to take a breather.”* — Passionate technologist,"
        " developer, and creative builder based in Cebu City, Philippines."
    )
    st.divider()
    st.text("Raised in Cebu City, Philippines, I am a passionate technologist and creative builder with a deep enthusiasm for software development, graphic design, and video editing.")

 
    

with col2:
    st.image(os.path.join(os.getcwd(), "static", "1.png"))

with st.sidebar:
    # Profile Picture (using use_container_width to make it responsive)
    st.image(os.path.join(os.getcwd(), "static", "ken2.png"), width='stretch')
    
    # Core Identity
    st.markdown("## Ken N. Horigome")
    st.caption("BS Computer Science — 3rd Year")
    st.caption("📍 Cebu City, Philippines")
    
    st.divider()
    
    # Personal Philosophy / Bio
    st.markdown('*"Always take time to take a breather."*')
    st.markdown(
        "Passionate technologist, developer, and creative builder focusing on "
        "human-centered software."
    )
    
    st.divider()
    
    # Contact Links
    st.markdown("### Connect with Me!")
    st.markdown("📧 [spicytaku@gmail.com](mailto:spicytaku@gmail.com)")
    st.markdown("📞 +63 961 050 3087")
    st.markdown("🐙 [GitHub](https://github.com/keneyboi)")
    st.markdown("💼 [LinkedIn](https://www.linkedin.com/in/ken-horigome-916808430)")
    
    st.space("medium")
    
    resume_path = os.path.join(os.getcwd(), "static", "Horigome_CV.pdf")

    # Check if the file exists to prevent errors during development
    if os.path.exists(resume_path):
      with open(resume_path, "rb") as file:
        pdf_data = file.read()
    else:
      pdf_data = b"Dummy Content"  # Fallback if file isn't found yet

    st.download_button(
        label="📄 Download Resume",
        data=pdf_data,
        file_name="Horigome_CV.pdf",
        mime="application/pdf",
        width="stretch",
    )
    
tab1, tab2, tab3, tab4 = st.tabs(
["Overview", "Repositories", "Skills", "Contact"])


with tab1:
    st.header("Overview")
    st.subheader("Autobiography & Background")
    st.markdown("Get to know more about me, from my roots, to my passions")
    st.divider()
    bio_col1, bio_col2 = st.columns(2, border=True)

    
    with bio_col1:
        st.image(os.path.join(os.getcwd(), "static", "old_ken.jpg"))

    with bio_col2:
        
        st.space("medium")
        st.subheader("Roots & Journey")
        st.write(
            "Growing up in Cebu City as a half-Japanese kid with a lifelong passion for art, I naturally evolved into a tech nerd fascinated by how software and hardware intersect. Long before I started writing clean code, I was already sketching, designing, and creating a creative foundation that now fuels my work as a software developer, graphic designer, and video editor."
        )
        
    st.divider()
        
    bio_col1, bio_col2 = st.columns(2, border=True)

    
    with bio_col1:
        st.space("large")
        st.subheader("Interests & Passions", text_alignment="right")
        st.markdown(
            "I thrive at the intersection of **engineering and design**. Whether"
            " it's architecting a web application, designing custom user"
            " interfaces, or editing visual media, I enjoy building tools that"
            " are both highly functional and aesthetically pleasing. I am always eager to experiment with new technologies and frameworks.", text_alignment="right"
        )

    with bio_col2:

        st.image(os.path.join(os.getcwd(), "static", "video.jpg"))
    
    st.divider()
    bio_col1, bio_col2 = st.columns(2, border=True)
    
        
    with bio_col1:
        st.image(os.path.join(os.getcwd(), "static", "parangal.png"))

    with bio_col2:
        st.space("medium")
        st.subheader("Education Journey")
        st.markdown(
            "I am currently an undergraduate student pursuing a **Bachelor of"
            " Science in Computer Science** at **Cebu Institute of Technology –"
            " University** (entering my 3rd year, section F2). Recognized as a"
            " *Parangal Awardee*, my academic path has been heavily shaped by"
            " rigorous problem-solving and modern technical stacks, with **Applied"
            " AI** standing out as my favorite coursework."
        )
    
    st.divider()
    st.subheader("Key Milestones")
    st.markdown(
        "- **Cardbooth Studio (2026):** Created a niche proprietary photobooth"
        " platform tailored for trading card arts like Pokémon and Vanguard."
    )
    st.markdown(
        "- **Marca:** Co-developed and launched a high-throughput universal ID"
        " attendance system designed for large-scale events, currently"
        " deployed at the University of Cebu – College of Nursing."
    )
    st.markdown(
        "- **Social Media Advertising:** Collaborated with brand-names such as McDonald's for advertising"
        " and skincare brands like Vitabears and Originote"
    )

    st.divider()


with tab2:
    st.header("Repositories")
    st.subheader("Personal Projects & Collaborative Work")
    st.markdown("Here are some of my most recent projects in Software Development.",)
    st.divider()
    col1, col2, col3 = st.columns(3, border=True)
    
    
    with col1:
        
        st.image(os.path.join(os.getcwd(), "static", "marca.png")) 
        st.header("Marca")
        st.markdown("*Universal Event Attendance Tracking System*")
        
        st.divider()
        st.markdown("**Role:** UI/UX Designer & Software Developer")
        st.markdown("`Python` `Django` `HTML5` `CSS3` `JavaScript`")
        st.markdown("**Overview**: A high-throughput attendance management platform engineered for large-scale events. Marca utilizes a universal identifier system (Marca ID) to facilitate rapid badge scanning and real-time attendance logging.")
        st.markdown("**Impact & Status:**: Currently deployed and actively used by the University of Cebu – College of Nursing for departmental events and daily tracking.")
    
    with col2:
        st.image(os.path.join(os.getcwd(), "static", "cardbooth.png")) 
        st.header("Cardbooth")
        st.markdown("*Proprietary Photobooth Engine for Custom Card Art*")
        st.divider()
        st.markdown("**Role:** Sole Developer")
        st.markdown("`Python` `Django` `HTML5` `CSS3` `JavaScript`")
        st.markdown("**Overview**: An interactive application designed to generate themed photobooth frames and digital keepsakes tailored specifically for trading card communities. Features custom card layout rendering inspired by Pokémon, Cardfight!! Vanguard, and bespoke designs.")
        st.markdown("**Impact & Status:**: Established in 2026 as a standalone proprietary photobooth suite for card collectors and pop-culture events.")
        
    with col3:
        st.image(os.path.join(os.getcwd(), "static", "tix.png")) 
        st.header("TIX.org")
        st.markdown("*Centralized Organizational Task & Ticketing Platform*")
        st.divider()
        st.markdown("**Role:** Software Developer & UI/UX Designer")
        st.markdown("`Java` `JavaFX`")
        st.markdown("**Overview**: A Desktop GUI application engineered to streamline organizational productivity. TIX.org enables teams to create, delegate, update, and track tasks within a single collaborative dashboard.")
        st.markdown("**Impact & Status:**: Promotes active team participation and member voluntarism by offering both direct task delegation and self-assignment workflows.")
        
    st.space("medium")
    
    st.header("Other Repositories", text_alignment="center")
    st.markdown(
        "Smaller tools, academic builds, and supplementary utilities.", text_alignment="center"
    )
    
    st.space('medium')


    other_col1, other_col2 = st.columns(2, border=True)

    with other_col1:
        st.markdown("### 🔹 SafeDismiss")
        st.markdown(
            "Real-time school dismissal tracking application built with a robust"
            " backend controller."
        )
        st.markdown("`Java` `Spring Boot` `Database Schema`")

        st.divider()

        st.markdown("### 🔹 G-Split")
        st.markdown(
            "Customizable payment-splitting digital wallet concept and pitch built"
            " for local micro-merchants."
        )
        st.markdown("`FinTech` `UI/UX Design` `GCash Integration`")

    with other_col2:
        st.markdown("### 🔹 Project Lighthouse")
        st.markdown(
            "Control panel application for managing physical Safe Haven emergency"
            " locations and staff protocols."
        )
        st.markdown("`Python` `Django` `Control Panel`")
        st.divider()

        st.markdown("### 🔹 Portfolio & RAG Experiments")
        st.markdown(
            "Local Retrieval-Augmented Generation system indexed with company policy"
            " documents and custom UI."
        )
        st.markdown("`Python` `ChromaDB` `Ollama (Qwen/Llama)`")
        
    st.divider()
        
        
with tab3:
    st.header("Skills") 
    st.subheader("Technical Proficiency and Skills Matrix")
    st.markdown(
        "A comprehensive breakdown of my core technical stack, frameworks, and"
        " multidisciplinary experience."
    )
    st.divider()

    st.subheader("Technologies Used")
    
    item1, item2, item3, item4, item5 = st.columns(5, border=True)
    
    with item1:
        st.image(os.path.join(os.getcwd(), "static", "photoshop.png"), width='stretch')
        st.caption("Adobe Photoshop", text_alignment="center")
    with item2:
        st.image(os.path.join(os.getcwd(), "static", "indesign.svg"), width='stretch')
        st.caption("Adobe Indesign", text_alignment="center")
    with item3:
        st.image(os.path.join(os.getcwd(), "static", "illustrator.svg"), width='stretch')
        st.caption("Adobe Illustrator", text_alignment="center")
    with item4:
        st.image(os.path.join(os.getcwd(), "static", "vn.png"), width='stretch')
        st.caption("VN", text_alignment="center")
        
    with item5:
        st.image(os.path.join(os.getcwd(), "static", "figma.png"), width='stretch')
        st.caption("Figma", text_alignment="center")


    st.subheader("Developer Identity")

    st.code(
        """
# Full-Stack Developer & Creative Technologist Profile
developer = {
    "name": "Ken Horigome",
    "role": "Full-Stack Software Developer & Creative Technologist",
    "background": (
        "3rd-Year BS Computer Science Student at CIT-U | Half-Japanese,"
        " Cebu-based"
    ),
    "primary_focus": (
        "Building user-centric software with robust backend systems, blending"
        " technical logic with modern design"
    ),
    "core_specializations": [
        "Web & App Development (Django, Spring Boot, Blazor, React)",
        "Model Harnessing & Local RAG Development (Ollama, ChromaDB)",
        "UI/UX Design & Branding (Adobe Photoshop, Figma, Tailwind CSS)",
        "Creative Media Production (Adobe Premiere Pro, Videography & Editing)",
    ],
    "philosophy": (
        "Always take time to take a breather — combining engineering precision"
        " with clean, intentional design."
    ),
}
""",
        language="python",
    )
    st.space('small')
    col_skills_left, col_skills_right = st.columns(2, border=True)
    with col_skills_right:
        st.subheader("Core Technologies and Languages")
        st.markdown(
            "• **Programming Languages:** `Python` `Java` `C#` `C++` `C` `Kotlin`"
        )
        st.markdown("• **Web Fundamentals:** `HTML5` `CSS3` `JavaScript`")
    with col_skills_left:
        st.subheader("Frameworks and Tooling")
        st.markdown(
            "• **Backend / Full-Stack:** `Django` `Spring Boot` `Blazor`\n•"
            " **Styling and UI:** `Tailwind CSS` `JavaFX`\n**Workflow and"
            " DevOps:** `Git` `GitHub` `EAS CLI`"
        )


    st.divider()
    stat2, stat3, stat4 = st.columns(3)
    stat2.metric("Design Experience", "4 Years", "Graphics")
    stat3.metric("Video Editing", "3 Years", "Freelance")
    stat4.metric("Key Projects", "4+", "Production")
    st.divider()

with tab4:
    st.header("Contact") 
    st.subheader("Let's Build Something Exceptional Together")
    st.markdown(
        "Whether you have a project in mind, a prospective collaboration, or just want to "
        "discuss software and creative design—my inbox is always open."
    )

    st.divider()

    contact_col1, contact_col2, contact_col3 = st.columns(3)

    with contact_col1:
        with st.container(border=True):
            st.markdown("### Email")
            st.markdown("*Direct Inbox*")
            st.markdown("[spicytaku@gmail.com](mailto:spicytaku@gmail.com)")

    with contact_col2:
        with st.container(border=True):
            st.markdown("### GitHub")
            st.markdown("*Code & Repositories*")
            st.markdown("[@keneyboi](https://github.com/keneyboi)")

    with contact_col3:
        with st.container(border=True):
            st.markdown("### LinkedIn")
            st.markdown("*Professional Network*")
            st.markdown("[Ken Horigome](https://www.linkedin.com/in/ken-horigome-916808430)")

    st.write("") 

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email") 
        message = st.text_area("Your Message")
        
        if st.form_submit_button("Send"):
            st.success(f"Thank you for reaching out, {name}! I'll get back to you soon.")