"""
THIS FILE IS AUTOGENERATED.

DO NOT MODIFY.

INSTEAD, RUN scripts/scrape_categories.py
"""

from enum import Enum


class ArxivCategory(Enum):
    stat_AP = 1  # Statistics - Applications
    stat_CO = 2  # Statistics - Computation
    stat_ML = 3  # Statistics - Machine Learning
    stat_ME = 4  # Statistics - Methodology
    stat_TH = 5  # Statistics - Theory
    q_bio_BM = 6  # Quantitative Biology - Biomolecules
    q_bio_CB = 7  # Quantitative Biology - Cell Behavior
    q_bio_GN = 8  # Quantitative Biology - Genomics
    q_bio_MN = 9  # Quantitative Biology - Molecular Networks
    q_bio_NC = 10  # Quantitative Biology - Neurons and Cognition
    q_bio_OT = 11  # Quantitative Biology - Other
    q_bio_PE = 12  # Quantitative Biology - Populations and Evolution
    q_bio_QM = 13  # Quantitative Biology - Quantitative Methods
    q_bio_SC = 14  # Quantitative Biology - Subcellular Processes
    q_bio_TO = 15  # Quantitative Biology - Tissues and Organs
    cs_AR = 16  # Computer Science - Architecture
    cs_AI = 17  # Computer Science - Artificial Intelligence
    cs_CL = 18  # Computer Science - Computation and Language
    cs_CC = 19  # Computer Science - Computational Complexity
    cs_CE = 20  # Computer Science - Computational Engineering; Finance; and Science
    cs_CG = 21  # Computer Science - Computational Geometry
    cs_GT = 22  # Computer Science - Computer Science and Game Theory
    cs_CV = 23  # Computer Science - Computer Vision and Pattern Recognition
    cs_CY = 24  # Computer Science - Computers and Society
    cs_CR = 25  # Computer Science - Cryptography and Security
    cs_DS = 26  # Computer Science - Data Structures and Algorithms
    cs_DB = 27  # Computer Science - Databases
    cs_DL = 28  # Computer Science - Digital Libraries
    cs_DM = 29  # Computer Science - Discrete Mathematics
    cs_DC = 30  # Computer Science - Distributed; Parallel; and Cluster Computing
    cs_GL = 31  # Computer Science - General Literature
    cs_GR = 32  # Computer Science - Graphics
    cs_HC = 33  # Computer Science - Human-Computer Interaction
    cs_IR = 34  # Computer Science - Information Retrieval
    cs_IT = 35  # Computer Science - Information Theory
    cs_LG = 36  # Computer Science - Learning
    cs_LO = 37  # Computer Science - Logic in Computer Science
    cs_MS = 38  # Computer Science - Mathematical Software
    cs_MA = 39  # Computer Science - Multiagent Systems
    cs_MM = 40  # Computer Science - Multimedia
    cs_NI = 41  # Computer Science - Networking and Internet Architecture
    cs_NE = 42  # Computer Science - Neural and Evolutionary Computing
    cs_NA = 43  # Computer Science - Numerical Analysis
    cs_OS = 44  # Computer Science - Operating Systems
    cs_OH = 45  # Computer Science - Other
    cs_PF = 46  # Computer Science - Performance
    cs_PL = 47  # Computer Science - Programming Languages
    cs_RO = 48  # Computer Science - Robotics
    cs_SE = 49  # Computer Science - Software Engineering
    cs_SD = 50  # Computer Science - Sound
    cs_SC = 51  # Computer Science - Symbolic Computation
    nlin_AO = 52  # Nonlinear Sciences - Adaptation and Self-Organizing Systems
    nlin_CG = 53  # Nonlinear Sciences - Cellular Automata and Lattice Gases
    nlin_CD = 54  # Nonlinear Sciences - Chaotic Dynamics
    nlin_SI = 55  # Nonlinear Sciences - Exactly Solvable and Integrable Systems
    nlin_PS = 56  # Nonlinear Sciences - Pattern Formation and Solitons
    math_AG = 57  # Mathematics - Algebraic Geometry
    math_AT = 58  # Mathematics - Algebraic Topology
    math_AP = 59  # Mathematics - Analysis of PDEs
    math_CT = 60  # Mathematics - Category Theory
    math_CA = 61  # Mathematics - Classical Analysis and ODEs
    math_CO = 62  # Mathematics - Combinatorics
    math_AC = 63  # Mathematics - Commutative Algebra
    math_CV = 64  # Mathematics - Complex Variables
    math_DG = 65  # Mathematics - Differential Geometry
    math_DS = 66  # Mathematics - Dynamical Systems
    math_FA = 67  # Mathematics - Functional Analysis
    math_GM = 68  # Mathematics - General Mathematics
    math_GN = 69  # Mathematics - General Topology
    math_GT = 70  # Mathematics - Geometric Topology
    math_GR = 71  # Mathematics - Group Theory
    math_HO = 72  # Mathematics - History and Overview
    math_IT = 73  # Mathematics - Information Theory
    math_KT = 74  # Mathematics - K-Theory and Homology
    math_LO = 75  # Mathematics - Logic
    math_MP = 76  # Mathematics - Mathematical Physics
    math_MG = 77  # Mathematics - Metric Geometry
    math_NT = 78  # Mathematics - Number Theory
    math_NA = 79  # Mathematics - Numerical Analysis
    math_OA = 80  # Mathematics - Operator Algebras
    math_OC = 81  # Mathematics - Optimization and Control
    math_PR = 82  # Mathematics - Probability
    math_QA = 83  # Mathematics - Quantum Algebra
    math_RT = 84  # Mathematics - Representation Theory
    math_RA = 85  # Mathematics - Rings and Algebras
    math_SP = 86  # Mathematics - Spectral Theory
    math_ST = 87  # Mathematics - Statistics
    math_SG = 88  # Mathematics - Symplectic Geometry
    astro_ph = 89  # Astrophysics
    cond_mat_dis_nn = 90  # Physics - Disordered Systems and Neural Networks
    cond_mat_mes_hall = 91  # Physics - Mesoscopic Systems and Quantum Hall Effect
    cond_mat_mtrl_sci = 92  # Physics - Materials Science
    cond_mat_other = 93  # Physics - Other
    cond_mat_soft = 94  # Physics - Soft Condensed Matter
    cond_mat_stat_mech = 95  # Physics - Statistical Mechanics
    cond_mat_str_el = 96  # Physics - Strongly Correlated Electrons
    cond_mat_supr_con = 97  # Physics - Superconductivity
    gr_qc = 98  # General Relativity and Quantum Cosmology
    hep_ex = 99  # High Energy Physics - Experiment
    hep_lat = 100  # High Energy Physics - Lattice
    hep_ph = 101  # High Energy Physics - Phenomenology
    hep_th = 102  # High Energy Physics - Theory
    math_ph = 103  # Mathematical Physics
    nucl_ex = 104  # Nuclear Experiment
    nucl_th = 105  # Nuclear Theory
    physics_acc_ph = 106  # Physics - Accelerator Physics
    physics_ao_ph = 107  # Physics - Atmospheric and Oceanic Physics
    physics_atom_ph = 108  # Physics - Atomic Physics
    physics_atm_clus = 109  # Physics - Atomic and Molecular Clusters
    physics_bio_ph = 110  # Physics - Biological Physics
    physics_chem_ph = 111  # Physics - Chemical Physics
    physics_class_ph = 112  # Physics - Classical Physics
    physics_comp_ph = 113  # Physics - Computational Physics
    physics_data_an = 114  # Physics - Data Analysis; Statistics and Probability
    physics_flu_dyn = 115  # Physics - Fluid Dynamics
    physics_gen_ph = 116  # Physics - General Physics
    physics_geo_ph = 117  # Physics - Geophysics
    physics_hist_ph = 118  # Physics - History of Physics
    physics_ins_det = 119  # Physics - Instrumentation and Detectors
    physics_med_ph = 120  # Physics - Medical Physics
    physics_optics = 121  # Physics - Optics
    physics_ed_ph = 122  # Physics - Physics Education
    physics_soc_ph = 123  # Physics - Physics and Society
    physics_plasm_ph = 124  # Physics - Plasma Physics
    physics_pop_ph = 125  # Physics - Popular Physics
    physics_space_ph = 126  # Physics - Space Physics
    quant_ph = 127  # Quantum Physics


arxiv_category_map = {
    ArxivCategory.stat_AP: 'stat.AP',
    ArxivCategory.stat_CO: 'stat.CO',
    ArxivCategory.stat_ML: 'stat.ML',
    ArxivCategory.stat_ME: 'stat.ME',
    ArxivCategory.stat_TH: 'stat.TH',
    ArxivCategory.q_bio_BM: 'q-bio.BM',
    ArxivCategory.q_bio_CB: 'q-bio.CB',
    ArxivCategory.q_bio_GN: 'q-bio.GN',
    ArxivCategory.q_bio_MN: 'q-bio.MN',
    ArxivCategory.q_bio_NC: 'q-bio.NC',
    ArxivCategory.q_bio_OT: 'q-bio.OT',
    ArxivCategory.q_bio_PE: 'q-bio.PE',
    ArxivCategory.q_bio_QM: 'q-bio.QM',
    ArxivCategory.q_bio_SC: 'q-bio.SC',
    ArxivCategory.q_bio_TO: 'q-bio.TO',
    ArxivCategory.cs_AR: 'cs.AR',
    ArxivCategory.cs_AI: 'cs.AI',
    ArxivCategory.cs_CL: 'cs.CL',
    ArxivCategory.cs_CC: 'cs.CC',
    ArxivCategory.cs_CE: 'cs.CE',
    ArxivCategory.cs_CG: 'cs.CG',
    ArxivCategory.cs_GT: 'cs.GT',
    ArxivCategory.cs_CV: 'cs.CV',
    ArxivCategory.cs_CY: 'cs.CY',
    ArxivCategory.cs_CR: 'cs.CR',
    ArxivCategory.cs_DS: 'cs.DS',
    ArxivCategory.cs_DB: 'cs.DB',
    ArxivCategory.cs_DL: 'cs.DL',
    ArxivCategory.cs_DM: 'cs.DM',
    ArxivCategory.cs_DC: 'cs.DC',
    ArxivCategory.cs_GL: 'cs.GL',
    ArxivCategory.cs_GR: 'cs.GR',
    ArxivCategory.cs_HC: 'cs.HC',
    ArxivCategory.cs_IR: 'cs.IR',
    ArxivCategory.cs_IT: 'cs.IT',
    ArxivCategory.cs_LG: 'cs.LG',
    ArxivCategory.cs_LO: 'cs.LO',
    ArxivCategory.cs_MS: 'cs.MS',
    ArxivCategory.cs_MA: 'cs.MA',
    ArxivCategory.cs_MM: 'cs.MM',
    ArxivCategory.cs_NI: 'cs.NI',
    ArxivCategory.cs_NE: 'cs.NE',
    ArxivCategory.cs_NA: 'cs.NA',
    ArxivCategory.cs_OS: 'cs.OS',
    ArxivCategory.cs_OH: 'cs.OH',
    ArxivCategory.cs_PF: 'cs.PF',
    ArxivCategory.cs_PL: 'cs.PL',
    ArxivCategory.cs_RO: 'cs.RO',
    ArxivCategory.cs_SE: 'cs.SE',
    ArxivCategory.cs_SD: 'cs.SD',
    ArxivCategory.cs_SC: 'cs.SC',
    ArxivCategory.nlin_AO: 'nlin.AO',
    ArxivCategory.nlin_CG: 'nlin.CG',
    ArxivCategory.nlin_CD: 'nlin.CD',
    ArxivCategory.nlin_SI: 'nlin.SI',
    ArxivCategory.nlin_PS: 'nlin.PS',
    ArxivCategory.math_AG: 'math.AG',
    ArxivCategory.math_AT: 'math.AT',
    ArxivCategory.math_AP: 'math.AP',
    ArxivCategory.math_CT: 'math.CT',
    ArxivCategory.math_CA: 'math.CA',
    ArxivCategory.math_CO: 'math.CO',
    ArxivCategory.math_AC: 'math.AC',
    ArxivCategory.math_CV: 'math.CV',
    ArxivCategory.math_DG: 'math.DG',
    ArxivCategory.math_DS: 'math.DS',
    ArxivCategory.math_FA: 'math.FA',
    ArxivCategory.math_GM: 'math.GM',
    ArxivCategory.math_GN: 'math.GN',
    ArxivCategory.math_GT: 'math.GT',
    ArxivCategory.math_GR: 'math.GR',
    ArxivCategory.math_HO: 'math.HO',
    ArxivCategory.math_IT: 'math.IT',
    ArxivCategory.math_KT: 'math.KT',
    ArxivCategory.math_LO: 'math.LO',
    ArxivCategory.math_MP: 'math.MP',
    ArxivCategory.math_MG: 'math.MG',
    ArxivCategory.math_NT: 'math.NT',
    ArxivCategory.math_NA: 'math.NA',
    ArxivCategory.math_OA: 'math.OA',
    ArxivCategory.math_OC: 'math.OC',
    ArxivCategory.math_PR: 'math.PR',
    ArxivCategory.math_QA: 'math.QA',
    ArxivCategory.math_RT: 'math.RT',
    ArxivCategory.math_RA: 'math.RA',
    ArxivCategory.math_SP: 'math.SP',
    ArxivCategory.math_ST: 'math.ST',
    ArxivCategory.math_SG: 'math.SG',
    ArxivCategory.astro_ph: 'astro-ph',
    ArxivCategory.cond_mat_dis_nn: 'cond-mat.dis-nn',
    ArxivCategory.cond_mat_mes_hall: 'cond-mat.mes-hall',
    ArxivCategory.cond_mat_mtrl_sci: 'cond-mat.mtrl-sci',
    ArxivCategory.cond_mat_other: 'cond-mat.other',
    ArxivCategory.cond_mat_soft: 'cond-mat.soft',
    ArxivCategory.cond_mat_stat_mech: 'cond-mat.stat-mech',
    ArxivCategory.cond_mat_str_el: 'cond-mat.str-el',
    ArxivCategory.cond_mat_supr_con: 'cond-mat.supr-con',
    ArxivCategory.gr_qc: 'gr-qc',
    ArxivCategory.hep_ex: 'hep-ex',
    ArxivCategory.hep_lat: 'hep-lat',
    ArxivCategory.hep_ph: 'hep-ph',
    ArxivCategory.hep_th: 'hep-th',
    ArxivCategory.math_ph: 'math-ph',
    ArxivCategory.nucl_ex: 'nucl-ex',
    ArxivCategory.nucl_th: 'nucl-th',
    ArxivCategory.physics_acc_ph: 'physics.acc-ph',
    ArxivCategory.physics_ao_ph: 'physics.ao-ph',
    ArxivCategory.physics_atom_ph: 'physics.atom-ph',
    ArxivCategory.physics_atm_clus: 'physics.atm-clus',
    ArxivCategory.physics_bio_ph: 'physics.bio-ph',
    ArxivCategory.physics_chem_ph: 'physics.chem-ph',
    ArxivCategory.physics_class_ph: 'physics.class-ph',
    ArxivCategory.physics_comp_ph: 'physics.comp-ph',
    ArxivCategory.physics_data_an: 'physics.data-an',
    ArxivCategory.physics_flu_dyn: 'physics.flu-dyn',
    ArxivCategory.physics_gen_ph: 'physics.gen-ph',
    ArxivCategory.physics_geo_ph: 'physics.geo-ph',
    ArxivCategory.physics_hist_ph: 'physics.hist-ph',
    ArxivCategory.physics_ins_det: 'physics.ins-det',
    ArxivCategory.physics_med_ph: 'physics.med-ph',
    ArxivCategory.physics_optics: 'physics.optics',
    ArxivCategory.physics_ed_ph: 'physics.ed-ph',
    ArxivCategory.physics_soc_ph: 'physics.soc-ph',
    ArxivCategory.physics_plasm_ph: 'physics.plasm-ph',
    ArxivCategory.physics_pop_ph: 'physics.pop-ph',
    ArxivCategory.physics_space_ph: 'physics.space-ph',
    ArxivCategory.quant_ph: 'quant-ph'
}

# print(arxiv_category_map[ArxivCategory.cs_AI])
