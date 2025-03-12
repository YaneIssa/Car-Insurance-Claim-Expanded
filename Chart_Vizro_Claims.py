import vizro.models as vm
import vizro.plotly.express as px
from vizro import Vizro
import pandas as pd

# Load dataset
df_expanded = pd.read_csv('expanded_car_insurance_claim_kde_fixed.csv')

# Create a scatter matrix for numerical features and color by categorical feature
page = vm.Page(
    title="Car Insurance Claims Analysis",
    components=[
        vm.Graph(
            figure=px.scatter_matrix(
                df_expanded, 
                dimensions=["CREDIT_SCORE", "ANNUAL_MILEAGE", "SPEEDING_VIOLATIONS", "PAST_ACCIDENTS"],
                color="OUTCOME"  # Coloring by OUTCOME variable
            ),
        ),
    ],
)

dashboard = vm.Dashboard(pages=[page])

Vizro().build(dashboard).run()
    