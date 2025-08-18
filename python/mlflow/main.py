import hydra
from omegaconf import DictConfig, OmegaConf


@hydra.main(version_base=None, config_path="../config", config_name="default")
def load_config(cfg: DictConfig):
    """Yaml形式の設定ファイルを読み込む

    Decorator Args:
        - config_path: 設定ファイルが格納されているディレクトリ
        - config_name: 読み込む設定ファイルの名前（拡張子は不要）

    Notes:
        - 設定ファイルの拡張子でymlはNG。必ずyamlを使用すること。

    """
    return cfg
