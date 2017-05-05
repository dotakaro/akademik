# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _


class akademik(models.Model):
    _name = 'akademik.kursus'
    _rec_name = 'nama'

    nama = fields.Char("Nama Kursus", size=100, required=True)
    keterangan = fields.Text("Keterangan")
    penanggungjawab_id = fields.Many2one(comodel_name="res.users")
    session_id = fields.One2many(comodel_name="akademik.session",
                                 inverse_name="kursus_id",
                                 string="Sesi Kursus", ondelete="cascade")
    # @api.multi
    def _ceknama(self):
        for x in self:
             if x['nama']:
                if len(x['nama']) < 4 :
                    return False
        return True

    _constraints = [
        (_ceknama, 'Nama tidak boleh kosong', ['nama'])
    ]


class session(models.Model):
    _name = 'akademik.session'
    _rec_name = 'nama'

    nama = fields.Char("Nama Session", size=100)
    keterangan = fields.Text("Keterangan")
    kursus_id = fields.Many2one(comodel_name="akademik.kursus", string="Kursus")
    pengajar_id = fields.Many2one(comodel_name="res.partner", string="Pegajar")
    tanggal_mulai = fields.Date(string="Tanggal Mulai")
    durasi = fields.Integer(string="Durasi Waktu")
    kapasitas = fields.Integer(string="Kapasitas Ruangan")
    foto = fields.Binary()
    peserta_id = fields.One2many(comodel_name="akademik.peserta",
                                 inverse_name="session_id", string="Peserta")
    kapasitas_terpakai = fields.Float(string="Kapasitas Terisi",
                                      compute="_hitung_k")

    @api.constrains('nama')
    def _cek_nama(self):
        if not self.nama:
            # raise ValidationError("Nama Tidak Boleh Kosong")
             raise exceptions.except_orm(_('Perhatian'), _('Nama tidak boleh kosong'))
            # Decorator untuk menghitung kapasitas ruangan terpakai

    @api.depends('peserta_id', 'kapasitas')
    def _hitung_k(self):
        self.makanan='nasi'
        for rec in self:
            if rec.kapasitas > 0:
                rec.kapasitas_terpakai = 100 * len(rec.peserta_id) / rec.kapasitas
            else:
                rec.kapasitas_terpakai = 0.0

    @api.onchange('kapasitas')
    def _onchange_kapasitas(self):
        self._hitung_k()

class peserta(models.Model):
    _name = 'akademik.peserta'
    _rec_name = 'nama'

    nama = fields.Char("Nama", size=100)
    session_id = fields.Many2one(comodel_name="akademik.session", string="Session Kursus")
    partner_id = fields.Many2one(comodel_name="res.partner", string="Nama Peserta")

    # constraint untuk membatasi memasukkan peserta yang sama berulang kali
    _sql_constraints = [
        ('unique_data', 'UNIQUE(session_id, partner_id)',
         'Anda tidak dapat mendaftarkan peserta yang sama berulang kali'),
        ('unique_id', 'UNIQUE(nama)', 'Nomor peserta harus unique')
    ]

    def _check_name(self):
        for val in self:
            if val['nama']:
                if len(val['nama']) < 4:
                    return False
        return True

    _constraints = [
        (_check_name, 'ID Harus lebih dari 4 digit', ['nama'])
    ]


class partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    is_pengajar = fields.Boolean(string="Pengajar")
    nama_ortu = fields.Char(string="Nama orangtua/wali", size=100)

