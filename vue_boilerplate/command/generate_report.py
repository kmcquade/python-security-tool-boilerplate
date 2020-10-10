import os
import logging
import webbrowser
import click
import click_log
from vue_boilerplate.output.report import HTMLReport

logger = logging.getLogger()
click_log.basic_config(logger)


@click.command()
@click.option(
    "--output",
    required=False,
    type=click.Path(exists=True),
    default=os.getcwd(),
    help="Output directory.",
)
@click.option(
    "--skip-open-report",
    required=False,
    default=False,
    is_flag=True,
    help="Don't open the HTML report in the web browser after creating. "
    "This helps when running the report in automation.",
)
@click_log.simple_verbosity_option(logger)
def generate_report(output, skip_open_report):
    """Generate an HTML Report that visualizes some JSON"""

    # The scan returns some JSON
    data = run_scan()

    # Feed the JSON in and get the rendered HTML report
    rendered_html_report = get_report(data)

    # Write the HTML report to the specified directory
    html_output_file = os.path.join(output, f"report.html")
    logger.info("Saving the report to %s", html_output_file)
    if os.path.exists(html_output_file):
        os.remove(html_output_file)
    with open(html_output_file, "w") as f:
        f.write(rendered_html_report)
    print(f"Wrote HTML results to: {html_output_file}")

    # Open the report in the browser automatically by default
    if not skip_open_report:
        print("Opening the HTML report")
        url = "file://%s" % os.path.abspath(html_output_file)
        webbrowser.open(url, new=2)


def run_scan():
    """This is where your amazing security tool returns JSON that your HTML report will parse."""
    data = [
        dict(first_name="Joe", last_name="Biden", city="DC"),
        dict(first_name="Kamala", last_name="Harris", city="DC"),
        dict(first_name="Nancy", last_name="Pelosi", city="DC"),
    ]
    return data


def get_report(json_scan_data):
    """This is where you process the data, feed it into the HTML report."""
    # Parse through the data to scan
    html_report = HTMLReport(
        results=json_scan_data,
    )
    # Feed it into the HTML report with Jinja
    rendered_report = html_report.get_html_report()
    # Then return the HTML report as a really fat string
    return rendered_report
