from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile


def generate_pdf_report(
    followers,
    engagement_rate,
    posts_per_week,
    growth_index,
    saturation_score,
    consistency_score,
    monetization_score,
    primary_lever,
    secondary_lever,
    ai_strategy
):

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")

    c = canvas.Canvas(temp_file.name, pagesize=letter)

    y = 750

    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, y, "Creator's Lab Growth Report")

    y -= 40
    c.setFont("Helvetica", 12)

    c.drawString(50, y, f"Followers: {followers}")
    y -= 20

    c.drawString(50, y, f"Engagement Rate: {engagement_rate}%")
    y -= 20

    c.drawString(50, y, f"Posts per Week: {posts_per_week}")
    y -= 40

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Growth Intelligence")

    y -= 30
    c.setFont("Helvetica", 12)

    c.drawString(50, y, f"Growth Potential Index: {growth_index}")
    y -= 20

    c.drawString(50, y, f"Saturation Risk: {saturation_score}")
    y -= 20

    c.drawString(50, y, f"Consistency Score: {consistency_score}")
    y -= 20

    c.drawString(50, y, f"Monetization Readiness: {monetization_score}")
    y -= 40

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Strategic Insights")

    y -= 30
    c.setFont("Helvetica", 12)

    c.drawString(50, y, f"Primary Growth Lever: {primary_lever}")
    y -= 20

    c.drawString(50, y, f"Secondary Opportunity: {secondary_lever}")
    y -= 40

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "AI Growth Strategy")

    y -= 30
    c.setFont("Helvetica", 11)

    for line in ai_strategy.split("\n"):
        c.drawString(50, y, line[:90])
        y -= 15

    c.save()

    return temp_file.name