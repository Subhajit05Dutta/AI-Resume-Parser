import tempfile
from pathlib import Path

import streamlit as st

from Resume_Parser import (
    read_resume,
    parse_resume,
    extract_job_information,
    final_score
)


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Resume Parser",
    page_icon="📄",
    layout="wide"
)


# ============================================================
# HEADER
# ============================================================

st.title("📄 AI Resume Parser")

st.write(
    "Analyze your resume against any job description "
    "using AI-powered resume parsing and ATS scoring."
)

st.divider()


# ============================================================
# JOB DESCRIPTION
# ============================================================

st.subheader("💼 Job Description")

job_description = st.text_area(
    "Paste the complete job description below:",
    height=300,
    placeholder=(
        "Example:\n\n"
        "We are looking for a Software Engineer with "
        "experience in Python, SQL, AWS and REST APIs..."
    )
)


# ============================================================
# RESUME UPLOAD
# ============================================================

st.subheader("📄 Upload Resume")

uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf", "docx"],
    help="Supported formats: PDF and DOCX"
)


# ============================================================
# ANALYZE
# ============================================================

if st.button(
    "🚀 Analyze Resume",
    type="primary",
    use_container_width=True
):

    # --------------------------------------------------------
    # VALIDATION
    # --------------------------------------------------------

    if not job_description.strip():

        st.warning(
            "⚠️ Please enter a job description first."
        )

        st.stop()

    if uploaded_file is None:

        st.warning(
            "⚠️ Please upload a resume first."
        )

        st.stop()


    try:

        # ====================================================
        # SAVE UPLOADED RESUME TEMPORARILY
        # ====================================================

        suffix = Path(
            uploaded_file.name
        ).suffix

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix
        ) as temp_file:

            temp_file.write(
                uploaded_file.getbuffer()
            )

            temp_path = Path(
                temp_file.name
            )


        # ====================================================
        # STEP 1 — READ RESUME
        # ====================================================

        with st.spinner(
            "📖 Reading resume..."
        ):

            resume_text = read_resume(
                temp_path
            )


        if not resume_text:

            st.error(
                "❌ Could not extract text from "
                "the uploaded resume."
            )

            st.stop()


        # ====================================================
        # STEP 2 — PARSE RESUME
        # ====================================================

        with st.spinner(
            "🤖 AI is extracting resume information..."
        ):

            parsed_resume = parse_resume(
                resume_text
            )


        # ====================================================
        # STEP 3 — ANALYZE JOB DESCRIPTION
        # ====================================================

        with st.spinner(
            "💼 AI is analyzing the job description..."
        ):

            job = extract_job_information(
                job_description
            )


        # ====================================================
        # STEP 4 — CALCULATE ATS SCORE
        # ====================================================

        with st.spinner(
            "📊 Calculating ATS compatibility..."
        ):

            result = final_score(
                job,
                parsed_resume
            )


        # ====================================================
        # RESULTS
        # ====================================================

        st.success(
            "✅ Resume analysis completed successfully!"
        )

        st.divider()


        # ====================================================
        # SCORE
        # ====================================================

        st.header("🎯 ATS Match Score")

        score = result.score

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Overall Match",
                f"{score:.1f}%"
            )

        with col2:

            st.metric(
                "Candidate",
                parsed_resume.name
                or "Not Found"
            )

        with col3:

            experience = (
                parsed_resume.total_experience_years
            )

            if experience is not None:

                experience_text = (
                    f"{experience} years"
                )

            else:

                experience_text = "Not Found"

            st.metric(
                "Experience",
                experience_text
            )


        # ====================================================
        # CANDIDATE INFORMATION
        # ====================================================

        st.divider()

        st.header("👤 Candidate Information")

        col1, col2 = st.columns(2)

        with col1:

            st.write("**Name**")

            st.write(
                parsed_resume.name
                or "Not found"
            )

            st.write("**Email**")

            st.write(
                parsed_resume.email
                or "Not found"
            )

        with col2:

            st.write("**Phone**")

            st.write(
                parsed_resume.phone
                or "Not found"
            )

            st.write("**Experience**")

            if parsed_resume.total_experience_years is not None:

                st.write(
                    f"{parsed_resume.total_experience_years} years"
                )

            else:

                st.write("Not specified")


        # ====================================================
        # SKILLS
        # ====================================================

        st.divider()

        st.header("🛠️ Skills")

        if parsed_resume.skills:

            for skill in parsed_resume.skills:

                st.write(
                    f"• {skill}"
                )

        else:

            st.write(
                "No skills found."
            )


        # ====================================================
        # EDUCATION
        # ====================================================

        st.header("🎓 Education")

        if parsed_resume.education:

            for education in parsed_resume.education:

                st.write(
                    f"• {education}"
                )

        else:

            st.write(
                "No education information found."
            )


        # ====================================================
        # EXPERIENCE
        # ====================================================

        st.header("💼 Experience")

        if parsed_resume.experiences:

            for experience in parsed_resume.experiences:

                role = (
                    experience.role
                    or "Role not specified"
                )

                st.markdown(
                    f"**{role}**"
                )

                if experience.company:

                    st.write(
                        f"Company: {experience.company}"
                    )

                if experience.duration:

                    st.write(
                        f"Duration: {experience.duration}"
                    )

                if experience.description:

                    st.write(
                        experience.description
                    )

                if experience.skills_used:

                    st.write(
                        "Skills used: "
                        + ", ".join(
                            experience.skills_used
                        )
                    )

                st.write("")

        else:

            st.write(
                "No experience information found."
            )


        # ====================================================
        # PROJECTS
        # ====================================================

        st.header("🚀 Projects")

        if parsed_resume.projects:

            for project in parsed_resume.projects:

                st.write(
                    f"• {project}"
                )

        else:

            st.write(
                "No projects found."
            )


        # ====================================================
        # CERTIFICATIONS
        # ====================================================

        st.header("🏆 Certifications")

        if parsed_resume.certifications:

            for certification in parsed_resume.certifications:

                st.write(
                    f"• {certification}"
                )

        else:

            st.write(
                "No certifications found."
            )


        # ====================================================
        # AI EVALUATION
        # ====================================================

        st.divider()

        st.header("🤖 AI Evaluation")

        details = result.details

        if isinstance(details, dict):

            for key, value in details.items():

                title = (
                    key
                    .replace("_", " ")
                    .title()
                )

                st.subheader(
                    title
                )

                if isinstance(value, list):

                    for item in value:

                        st.write(
                            f"• {item}"
                        )

                else:

                    st.write(
                        str(value)
                    )

        else:

            st.write(
                str(details)
            )


    except Exception as e:

        st.error(
            "❌ An error occurred while analyzing "
            "the resume."
        )

        st.exception(e)
