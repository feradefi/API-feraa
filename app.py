from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Data cuaca dengan lebih dari 10 entri
weather_data = [
    {"id": 1, "tanggal": "2024-11-01", "suhu": 28, "kelembapan": 60, "status": "Cerah", "kota": "Madura"},
    {"id": 2, "tanggal": "2024-11-02", "suhu": 27, "kelembapan": 65, "status": "Berawan", "kota": "Madura"},
    {"id": 3, "tanggal": "2024-11-03", "suhu": 29, "kelembapan": 70, "status": "Hujan", "kota": "Madura"},
    {"id": 4, "tanggal": "2024-11-04", "suhu": 30, "kelembapan": 75, "status": "Cerah", "kota": "Pamekasan"},
    {"id": 5, "tanggal": "2024-11-05", "suhu": 26, "kelembapan": 80, "status": "Hujan Ringan", "kota": "Sampang"},
    {"id": 6, "tanggal": "2024-11-06", "suhu": 28, "kelembapan": 55, "status": "Cerah", "kota": "Bangkalan"},
    {"id": 7, "tanggal": "2024-11-07", "suhu": 27, "kelembapan": 62, "status": "Berawan", "kota": "Madura"},
    {"id": 8, "tanggal": "2024-11-08", "suhu": 31, "kelembapan": 58, "status": "Cerah", "kota": "Madura"},
    {"id": 9, "tanggal": "2024-11-09", "suhu": 26, "kelembapan": 74, "status": "Hujan", "kota": "Sumenep"},
    {"id": 10, "tanggal": "2024-11-10", "suhu": 25, "kelembapan": 72, "status": "Berawan", "kota": "Madura"},
    {"id": 11, "tanggal": "2024-11-11", "suhu": 29, "kelembapan": 67, "status": "Cerah", "kota": "Pamekasan"},
    {"id": 12, "tanggal": "2024-11-12", "suhu": 28, "kelembapan": 63, "status": "Cerah", "kota": "Sampang"},
]

class WeatherList(Resource):
    def get(self):
        return {
            "error": False,
            "message": "success",
            "count": len(weather_data),
            "data": weather_data
        }

class WeatherDetail(Resource):
    def get(self, weather_id):
        weather_entry = next((item for item in weather_data if item["id"] == int(weather_id)), None)
        if weather_entry:
            return {
                "error": False,
                "message": "success",
                "data": weather_entry
            }
        return {"error": True, "message": "Weather entry not found"}, 404

class AddWeatherEntry(Resource):
    def post(self):
        data = request.get_json()
        new_entry = {
            "id": len(weather_data) + 1,
            "tanggal": data.get('tanggal'),
            "suhu": data.get('suhu'),
            "kelembapan": data.get('kelembapan'),
            "status": data.get('status'),
            "kota": data.get('kota')  # Menambahkan kota
        }
        weather_data.append(new_entry)
        return {
            "error": False,
            "message": "Weather entry added successfully",
            "data": new_entry
        }, 201

class UpdateWeatherEntry(Resource):
    def put(self, weather_id):
        data = request.get_json()
        weather_entry = next((item for item in weather_data if item["id"] == int(weather_id)), None)
        if weather_entry:
            weather_entry['tanggal'] = data.get('tanggal', weather_entry['tanggal'])
            weather_entry['suhu'] = data.get('suhu', weather_entry['suhu'])
            weather_entry['kelembapan'] = data.get('kelembapan', weather_entry['kelembapan'])
            weather_entry['status'] = data.get('status', weather_entry['status'])
            weather_entry['kota'] = data.get('kota', weather_entry['kota'])  # Menambahkan kota
            return {
                "error": False,
                "message": "Weather entry updated successfully",
                "data": weather_entry
            }
        return {"error": True, "message": "Weather entry not found"}, 404

class DeleteWeatherEntry(Resource):
    def delete(self, weather_id):
        global weather_data
        weather_data = [item for item in weather_data if item["id"] != int(weather_id)]
        return {
            "error": False,
            "message": "Weather entry deleted successfully"
        }

api.add_resource(WeatherList, '/weather')
api.add_resource(WeatherDetail, '/weather/<int:weather_id>')
api.add_resource(AddWeatherEntry, '/weather/add')
api.add_resource(UpdateWeatherEntry, '/weather/update/<int:weather_id>')
api.add_resource(DeleteWeatherEntry, '/weather/delete/<int:weather_id>')

if __name__ == '__main__':
    app.run(debug=True)
