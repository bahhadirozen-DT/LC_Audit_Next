class PortValidator:

    def validate(self, mt700, bl):

        r=[]

        lp=getattr(mt700,"port_of_loading",None)
        bp=getattr(bl,"port_of_loading",None)

        if lp and bp and lp.strip().upper()!=bp.strip().upper():
            r.append("PORT_OF_LOADING_MISMATCH")

        ld=getattr(mt700,"port_of_discharge",None)
        bd=getattr(bl,"port_of_discharge",None)

        if ld and bd and ld.strip().upper()!=bd.strip().upper():
            r.append("PORT_OF_DISCHARGE_MISMATCH")

        return r
