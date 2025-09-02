# API Endpoints Testing Commands

```bash
curl -i -X GET "http://localhost:5001/api/"


curl -i -X GET "http://localhost:5001/api/dams/"


curl -i -X GET "http://localhost:5001/api/dams/203042"


curl -i -X GET "http://localhost:5001/api/latest_data/"


curl -i -X GET "http://localhost:5001/api/latest_data/203042"


curl -i -X GET "http://localhost:5001/api/dam_resources/"


curl -i -X GET "http://localhost:5001/api/dam_resources/1"


curl -i -X GET "http://localhost:5001/api/specific_dam_analysis/"


curl -i -X GET "http://localhost:5001/api/specific_dam_analysis/203042"


curl -i -X GET "http://localhost:5001/api/overall_dam_analysis/"


curl -i -X GET "http://localhost:5001/api/overall_dam_analysis/2024-11-25"


curl -i -X GET "http://localhost:5001/api/dam_groups/"


curl -i -X GET "http://localhost:5001/api/dam_groups/small_dams"


curl -i -X GET "http://localhost:5001/api/dam_group_members/"

curl -i -X GET "http://localhost:5001/api/dam_group_members/small_dams"
```