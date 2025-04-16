from dataclasses import dataclass

@dataclass
class Organiz:
    kod_org: str
    name_org: str
    adress_org: str

@dataclass
class Prihvid:
    kod_prih_vid: str
    name_prih_vid: str
    
@dataclass
class Prih:
    kod_prih: str
    kod_prih_vid_v: str
    sum_prih: str
    data_prih: str
    prim_prih: str
    
@dataclass
class Prodvid:
    kod_prod_vid: str
    name_prod_vid: str
    
@dataclass
class Prod:
    kod_prod: str
    kod_prod_vid_v: str
    name_prod: str

@dataclass
class Visa:
    id_visa: str
    visa_n: str
    visa_nom: str
    visa_s: str
    
@dataclass
class Trati:
    kod_pokup: str
    kod_prod_tr: str
    kod_org_tr: str
    cena_tr: str
    kol_ed_tr: str
    data_tr: str
    prim_tr: str

    def __post_init__(self) -> None:
        self.prim_tr = f'{self.prim_tr} {self.kol_ed_tr}'
