REM pytest -v -s -m "sanity" --html=./reports/report.html test_cases/ --browser chrome

pytest -v -s -m "regression" --html=./reports/report.html test_cases/ --browser chrome
pytest -v -s -m "regression" --html=./reports/report.html test_cases/ --browser firefox

REM pytest -v -s -m "sanity or regression" --html=./reports/report.html test_cases/ --browser chrome

REM pytest -v -s -m "sanity and regression" --html=./reports/report.html test_cases/ --browser chrome
