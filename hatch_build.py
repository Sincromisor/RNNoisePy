from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomHook(BuildHookInterface):
    def initialize(self, version, build_data):
        # 「純粋Python」扱いをやめる（Root-Is-Purelib: false 相当）
        build_data["pure_python"] = False
        # バージョン/ABI/プラットフォームから最も具体的なタグを自動推定
        build_data["infer_tag"] = True
