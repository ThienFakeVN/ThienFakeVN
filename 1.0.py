import random, os, json

"""
KỂ CẢ KHI ĐÂY LÀ TRÒ CHƠI MÃ NGUỒN MỞ, ĐÙNG CHỈNH SỬA MÃ CỦA TRÒ CHƠI
NÓ CÓ THỂ DẪN ĐẾN CÁC LỖI KHÔNG LƯỜNG TRƯỚC!
"""

print('Bạn có 100 rúp Nga. Bạn định đi đầu tư.')
print('Chào mừng đến với \033[3mINVESTER: AMPLIFIED (v1.0)\033[0m!')

def action():
    print('')
    command = None
    command = input('Nhập một lệnh, như "start" để bắt đầu trò chơi, "story" để xem cốt truyện hay "?" để xem danh sách lệnh: ')
    if command.casefold() == 'start': play()
    elif command.casefold() == 'story': print('''
Bạn là nhà đầu tư của 3 công ty này:
    - Công ty \033[38;2;63;72;204mA\033[0m: Viết tắt của \033[38;2;63;72;204;4mA\033[38;2;63;72;204mđù\033[0m, phát triển chậm nhưng tốt và ổn định;
    - Công ty \033[38;2;163;73;164mB\033[0m: Viết tắt của, ờ... \033[38;2;163;73;164;4mT\033[38;2;163;73;164mhanh \033[38;2;163;73;164;4mB\033[38;2;163;73;164mình\033[0m? Vâng, \033[38;2;163;73;164;4mT\033[38;2;163;73;164mhanh \033[38;2;163;73;164;4mB\033[38;2;163;73;164mình\033[0m, phát triển trung bình;
    - Công ty \033[38;2;136;0;21mC\033[0m: Viết tắt của \033[38;2;136;0;21;4mC\033[38;2;136;0;21moin \033[38;2;136;0;21;4mC\033[38;2;136;0;21mard\033[0m, phát triển rất bất ổn. Chắc thằng chủ tịch công ty này đem tiền đầu tư đi đánh lô.
Lãi — lỗ của các công ty sẽ ảnh hưởng túi tiền của bạn và ảnh hưởng bao nhiêu tùy thuộc vào số tiền bạn đầu tư vào 3 công ty này.
Chúc 100 rúp Nga của bạn không bay màu!''')
    elif command.casefold() == 'help' or command.casefold() == '?' : print('''
ABOUTME/ABOUTUS     Hiển thị thông tin về tôi — người tạo ra trò chơi này
ABOUTUPDATE         Hiển thị thông tin về bản cập nhật
CREDITS             Hiển thị thông tin về bên sản xuất trò chơi
CWD                 Hiển thị thư mục làm việc hiện tại
HELP/?              Hiển thị danh sách lệnh có thể sử dụng tại khu vực action
READ                Đọc một tệp .json chứa dữ liệu trò chơi
START               Bắt đầu trò chơi
STORY               Kể câu truyện trong trò chơi
UPDATE              Tìm và thay đổi bản cập nhật của trò chơi (yêu cầu mô đun requests)''')
    elif command.casefold() == 'cwd': print(f'''
Thư mục làm việc hiện tại: {os.getcwd()}. Đây cũng là nơi các tệp trò chơi sẽ được lưu nếu bạn chọn lưu chúng.''')
    elif command.casefold() == 'read': read()
    elif command.casefold() == 'aboutme' or command.casefold() == 'aboutus': print('''
Tôi tên là Thiện, bạn có thể gọi tôi là ThienFakeVN hoặc ThieenjVN.
Tôi (chỉ có mình tôi) là người đã tạo ra trò chơi này. Đây cũng là trò chơi đầu tiên tôi làm.
Tôi làm ra những trò chơi miễn phí và mã nguồn mở, sử dụng màn hình Terminal, được viết bằng Python, có nội dung là những thứ vừa đơn giản vừa phức tạp vừa đơn giản mà tôi nghĩ ra trong đầu.
Tài khoản GitHub cho ai cần: ThienFakeVN.''')
    elif command.casefold() == 'credits' or command.casefold() == 'credit': print('''
\033[1mCREDITS — \033[3mINVESTER: AMPLIFIED (v1.0)\033[0m
\033[3mINVESTER: AMPLIFIED\033[0m là bản làm lại của \033[3mINVESTER\033[0m. Đây là trò chơi miễn phí và mã nguồn mở.
CHỊU TRÁCH NGHIỆM SẢN XUẤT     ThienFakeVN
NỘI DUNG TRÒ CHƠI              ThienFakeVN
VIẾT MÃ                        ThienFakeVN

\033[1mSPECIAL THANKS\033[0m
Ngân hàng Trung ương Liên Bang Nga (phát hành đồng rúp Nga, đồng tiền được sử dụng trong trò chơi là rúp Nga, nếu bạn chưa để ý)
Visual Studio Code (phần mềm tôi sử dụng để lập trình)
w3schools.com (nơi đầu tiên tôi bắt đầu học lập trình)
Đứa nào đó tên là Thanh Bình học cùng trường với tôi (công ty \033[38;2;163;73;164mB\033[0m trong trò chơi là viết tắt của \033[38;2;163;73;164;4mT\033[38;2;163;73;164mhanh \033[38;2;163;73;164;4mB\033[38;2;163;73;164mình\033[0m mà, đúng không?)
Màn hình Terminal nền đen chữ trắng (sử dụng mặc định cho các tệp lập trình)
Ngôn ngữ lập trình Python (ngôn ngữ tôi sử dụng để lập trình)
Và vâng, không thể thiếu, chính là các bạn! (những người đã chơi trò chơi này)''')
    elif command.casefold() == 'aboutupdate': print('''
\033[3mINVESTER: AMPLIFIED (v1.0)\033[0m là bản cập nhật đầu tiên của \033[3mINVESTER: AMPLIFIED\033[0m. Bản cập nhật gồm những nội dung sau:
    - Người chơi là nhà đầu tư của 3 công ty \033[38;2;63;72;204mA\033[0m, \033[38;2;163;73;164mB\033[0m và \033[38;2;136;0;21mC\033[0m. Người chơi ban đầu có 100 rúp Nga để đầu tư vào 3 công ty này;
    - Khu vực action có thể chạy các lệnh: ABOUTME, ABOUTUS, ABOUTUPDATE, CREDITS, CWD, HELP, START, STORY, ?;''')
    elif command.casefold() == 'update': update()
    else: print('Không hợp lệ, nhập "?" để xem danh sách các lệnh.')
    action()

def play(): 
    global money, game_seed, data_game, turns, A, B, C
    game_seed = input('Chọn một seed cho trò chơi (bỏ trống để có một seed ngẫu nhiên): ')
    if game_seed == '': game_seed = random.random()
    random.seed(game_seed)
    data_game = {'game':'invester', 'version': '1.0', 'seed': game_seed}
    money = 100
    turns = 1
    while turns >= 0:
        print('')
        print(f'Lượt {turns}')
        money_input()
        print('')
        A *= random.randint(-2, 5)
        B *= random.randint(-10, 10)
        C *= random.randint(-69, 50)
        money = money_remains + A + B + C
        print(f'''Tiền nhận được từ công ty \033[38;2;63;72;204mA\033[0m: {A};
Tiền nhận được từ công ty \033[38;2;163;73;164mB\033[0m: {B};
Tiền nhận được từ công ty \033[38;2;136;0;21mC\033[0m: {C};
Tổng số tiền sau lượt {turns} là {money}.''')
        data_game[f'turn {turns}'].update({'collected A': f'{A}', 'collected B': f'{B}', 'collected C': f'{C}', 'money collected': f'{money}'})
        if money <= 0: game_over()
        turns += 1

def money_input():
    global money, data_game, A, B, C, money_remains
    try: A, B, C = int(input('Chọn số tiền bạn đầu tư vào công ty \033[38;2;63;72;204mA\033[0m: ')), int(input('Chọn số tiền bạn đầu tư vào công ty \033[38;2;163;73;164mB\033[0m: ')), int(input('Chọn số tiền bạn đầu tư vào công ty \033[38;2;136;0;21mC\033[0m: '))
    except ValueError:
        print('Lỗi: Vui lòng nhập một số nguyên dương.')
        money_input()
    if A < 0 or B < 0 or C < 0:
        print('Lỗi: Không thể nhập số âm.')
        money_input()
    if A > money or B > money or C > money or A + B > money or B + C > money or A + C > money or A + B + C > money:
        print('Lỗi: Vung lòng không nhập quá số tiền hiện có.')
        money_input()
    if A + B + C < money:
        money_remains = money - (A + B + C)
        print(f'Bạn dùng {A + B + C} rúp đi đầu tư, {money_remains} rúp còn lại bạn cất vào trong túi.')
    if A + B + C == money:
        money_remains = 0
        print('Bạn dùng hết tiền đi đầu tư.')
    data_game.update({f'turn {turns}': {'chosen A': f'{A}', 'chosen B': f'{B}', 'chosen C': f'{C}'}})

def game_over():
    random.seed(None)
    print('')
    print('Bạn hết tiền! Trò chơi kết thúc!')
    print(f'Trước khi đi, seed của trò chơi của bạn là {game_seed}.')
    command = input(f'Và bạn có thể tải dữ liệu của trò chơi này vào một tệp .json bằng cách nhập "SAVE": ')
    if command.casefold() == 'save':
        game_code = random.randint(1, 999999999999999999999999)
        with open(f'invested{game_code}.json', 'w', encoding='utf-8') as invested:
            json.dump(data_game, invested, indent = 4)
        print(f'Đã xong! Vị trí của tệp: {os.getcwd()}\\invested{game_code}.json')
    action()

def read():
    print('')
    saved_data_location = input('Nhập địa chỉ của tệp .json: ')
    try: 
        with open(saved_data_location, 'r', encoding='utf-8') as saved_data_file:
            saved_data = json.load(saved_data_file)
    except FileNotFoundError:
        print('Lỗi: Không tìm thấy tệp nào tại địa chỉ này.')
        action()
    try:
        if saved_data['game'] == 'invester':
            print(f'''
Phiên bản: {saved_data['version']}
Seed: {saved_data['seed']}''')
            turns = 1
            while turns:
                print(f'''
Lượt {turns}:
    - A: {saved_data[f'turn {turns}']['chosen A']} => {saved_data[f'turn {turns}']['collected A']};
    - B: {saved_data[f'turn {turns}']['chosen B']} => {saved_data[f'turn {turns}']['collected B']};
    - C: {saved_data[f'turn {turns}']['chosen C']} => {saved_data[f'turn {turns}']['collected C']};
    - Tổng số tiền nhận được: {saved_data[f'turn {turns}']['money collected']}.''')
                turns += 1
                if int(saved_data[f'turn {turns - 1}']['money collected']) < 0: action()
    except KeyError:
        print('')
        print('Lỗi: Có vẻ như đây không phải là tệp có dữ liệu trò chơi này.')
        action()

def update():
    try: import requests
    except ModuleNotFoundError:
        print('Lỗi: Mô đun requests không được tìm thấy. Kiểm tra xem bạn đã cài đặt mô đun này chưa.')
        action()
    print('')
    updates = requests.get('https://raw.githubusercontent.com/ThienFakeVN/ThienFakeVN/refs/heads/invester/updates.py')
    environment = {}
    exec(updates.content, environment)
    chosen_update = input('Chọn bản cập nhật bạn muốn chơi: ')
    for update in environment['updates']:
        if update == chosen_update:
            print('Đã tìm thấy bản cập nhật.')
            command = input('Nhập "UPDATE" để cập nhật: ')
            if command.casefold() == 'update':
                file_path = os.path.abspath(__file__)
                update_content = requests.get(f'https://raw.githubusercontent.com/ThienFakeVN/ThienFakeVN/refs/heads/invester/{chosen_update}.py')
                with open(file_path, 'wb') as rewrite:
                    rewrite.write(update_content.content)
                    exit()
            else: action()
        print('Không tìm thấy bản cập nhật nào.')
    action()

print('''
(Gọi đây là khu vực action, nơi bạn sử dụng các lệnh)''')
action()
