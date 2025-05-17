import httpx
from django.core.files.storage import Storage
from django.core.files.base import ContentFile
from django.conf import settings

class SupabaseStorage(Storage):
    def __init__(self):
        self.url = settings.SUPABASE_URL
        self.key = settings.SUPABASE_KEY
        self.bucket = settings.SUPABASE_BUCKET
        self.headers = {
            "apikey": self.key,
            "Authorization": f"Bearer {self.key}"
        }

    def _get_upload_url(self, name):
        return f"{self.url}/storage/v1/object/{self.bucket}/{name}"

    def _open(self, name, mode="rb"):
        r = httpx.get(self._get_upload_url(name), headers=self.headers)
        return ContentFile(r.content)

    def _save(self, name, content):
        full_path = name
        r = httpx.put(
            f"{self.url}/storage/v1/object/{self.bucket}/{full_path}",
            headers=self.headers,
            content=content.read()
        )
        if r.status_code not in [200, 201]:
            raise Exception("Upload to Supabase failed: " + r.text)
        return full_path

    def url(self, name):
        return f"{self.url}/storage/v1/object/public/{self.bucket}/{name}"