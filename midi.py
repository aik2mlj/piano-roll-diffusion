import pretty_midi

if __name__ == "__main__":
    file = "./media/uncond_inp_below_ode_0.mid"
    midi = pretty_midi.PrettyMIDI(file)
    save = midi.write("./media/midi.mid")
