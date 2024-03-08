import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("./data/participa.gencat.cat-open-data-proposals.csv")
df = df[
    df["participatory_space/url"]
    == "http://participa.gencat.cat/processes/assembleaclima?participatory_process_slug=assembleaclima"
]
df["published_at"] = pd.to_datetime(df["published_at"], utc=True)
profile = ProfileReport(df, title="Profiling Report")

profile.to_file("proposals_report.html")
