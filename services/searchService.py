from scripts.automacaoWeb import automacaoWeb


def search(rede_social: str, perfil: str):
    ans = automacaoWeb(rede_social, perfil)
    return ans
