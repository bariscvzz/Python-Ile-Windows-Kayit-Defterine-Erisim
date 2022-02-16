from winreg import (
  ConnectRegistry,
  OpenKey,
  KEY_ALL_ACCESS,
  EnumValue,
  QueryInfoKey,
  HKEY_LOCAL_MACHINE,
  HKEY_CURRENT_USER
)
def enum_key(hive, subkey:str):
    with OpenKey(hive, subkey, 0, KEY_ALL_ACCESS) as key:
        num_of_values = QueryInfoKey(key)[1]
        for i in range(num_of_values):
            values = EnumValue(key, i)
            if values[0] == "LangID": continue
            print(*values[:-1], sep="\t")
if __name__ == "__main__":

    with ConnectRegistry(None, HKEY_LOCAL_MACHINE) as hklm_hive:
        print("\nVersiyon Bilgileri")
        print("-"*50)
        enum_key(hklm_hive, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")
        print("\nSistem Değişiklikleri")
        print("-"*50)
        enum_key(hklm_hive, r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment")
        print("\nBaşlatılan Programlar")
        print("-"*50)
        enum_key(hklm_hive, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run")
        print("\nSaat Dilimi")
        print("-"*50)
        enum_key(hklm_hive, r"SYSTEM\CurrentControlSet\Control\TimeZoneInformation")
        print("\nZararlı Yazılımlar tarafından shell girdi değerinin değiştirilmesi kontrol durumu")
        print("-"*50)
        enum_key(hklm_hive, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon")

    with ConnectRegistry(None, HKEY_CURRENT_USER) as hkcu_hive:
        print("\nÖnceden Çalıştırılan Uygulamalar")
        print("-"*50)
        enum_key(hkcu_hive, r"SOFTWARE\Classes\Local Settings\Software\Microsoft\Windows\Shell\MuiCache")
