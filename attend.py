"""
스터디 출석부 프로그램 (attend.py)
- 외부 라이브러리 없이 표준 라이브러리만 사용
- 출석 기록은 attendance.csv 파일에 저장됩니다.
"""

import csv
import os
from datetime import date

DATA_FILE = "attendance.csv"


def load_records():
    """CSV 파일에서 출석 기록을 읽어 리스트로 반환한다."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def save_record(record_date, name):
    """출석 한 건을 CSV 파일에 추가한다(append)."""
    file_exists = os.path.exists(DATA_FILE)
    with open(DATA_FILE, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:          # 파일이 없으면 헤더(제목 줄)를 먼저 쓴다
            writer.writerow(["date", "name"])
        writer.writerow([record_date, name])


def add_attendance():
    """출석 추가: 날짜(빈칸이면 오늘)와 이름을 입력받아 저장한다."""
    record_date = input("날짜 (YYYY-MM-DD, 엔터 시 오늘): ").strip()
    if record_date == "":
        record_date = date.today().isoformat()   # 예: 2024-05-20

    name = input("이름: ").strip()
    if name == "":
        print("⚠️  이름은 비워둘 수 없어요.\n")
        return

    save_record(record_date, name)
    print(f"✅ 출석 저장 완료: {record_date} / {name}\n")


def list_attendance():
    """전체 출석 목록을 날짜순으로 보여준다."""
    records = load_records()
    if not records:
        print("아직 출석 기록이 없어요.\n")
        return

    # 날짜 기준 정렬
    records.sort(key=lambda r: r["date"])

    print("\n===== 출석 목록 =====")
    for i, r in enumerate(records, start=1):
        print(f"{i:>3}. {r['date']}  {r['name']}")
    print(f"총 {len(records)}건\n")


def menu():
    """메뉴를 반복해서 보여주는 메인 루프."""
    while True:
        print("===== 스터디 출석부 =====")
        print("1) 출석 추가")
        print("2) 출석 목록 보기")
        print("3) 종료")
        choice = input("선택: ").strip()

        if choice == "1":
            add_attendance()
        elif choice == "2":
            list_attendance()
        elif choice == "3":
            print("프로그램을 종료합니다. 수고했어요! 👋")
            break
        else:
            print("1, 2, 3 중에서 골라주세요.\n")


if __name__ == "__main__":
    menu()
