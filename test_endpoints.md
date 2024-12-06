# API Endpoints Testing Commands

```bash
# Main Blueprint

curl -i -X GET "http://localhost:5001/api/"
# Dams Blueprint

# Get all dams
curl -i -X GET "http://localhost:5001/api/dams/"

# Get specific dam (Example: 203042 - Toonumbar Dam)
curl -i -X GET "http://localhost:5001/api/dams/203042"

# Latest Data Blueprint

# Get all latest data
curl -i -X GET "http://localhost:5001/api/latest_data/"

# Get latest data for a specific dam (Example: 203042 - Toonumbar Dam)
curl -i -X GET "http://localhost:5001/api/latest_data/203042"

# Dam Resources Blueprint

# Get all dam resources
curl -i -X GET "http://localhost:5001/api/dam_resources/"

# Get a specific dam resource (Example: resource_id = 1)
curl -i -X GET "http://localhost:5001/api/dam_resources/1"

# Specific Dam Analysis Blueprint

# Get all specific dam analyses
curl -i -X GET "http://localhost:5001/api/specific_dam_analysis/"

# Get specific dam analysis for a dam (Example: 203042 - Toonumbar Dam)
curl -i -X GET "http://localhost:5001/api/specific_dam_analysis/203042"

# Overall Dam Analysis Blueprint

# Get all overall dam analyses
curl -i -X GET "http://localhost:5001/api/overall_dam_analysis/"

# Get overall dam analysis for a specific date (Example: 2023-01-01)
curl -i -X GET "http://localhost:5001/api/overall_dam_analysis/2023-01-01"

# Dam Groups Blueprint

# Get all dam groups
curl -i -X GET "http://localhost:5001/api/dam_groups/"

# Get specific dam group (Example: small_dams)
curl -i -X GET "http://localhost:5001/api/dam_groups/small_dams"

# Dam Group Members Blueprint

# Get all dam group members
curl -i -X GET "http://localhost:5001/api/dam_group_members/"

# Get dam group members for a specific group (Example: small_dams)
curl -i -X GET "http://localhost:5001/api/dam_group_members/small_dams"
