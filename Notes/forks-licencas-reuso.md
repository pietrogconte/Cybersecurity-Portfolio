# Forks, Licenças e Reuso de Código — Resumo Prático

## O que é um fork

Cópia completa e independente de um repositório público, criada na sua conta. Você pode clonar, editar, commitar e dar push livremente, sem afetar o original. Pode sincronizar com o original depois ("Sync fork") e, opcionalmente, abrir um **Pull Request** se quiser contribuir suas mudanças de volta.

**Abrir PR nunca é obrigatório** — é uma escolha, não uma exigência técnica.

---

## Posso usar código de um fork como se fosse meu?

Depende inteiramente da **licença** do repositório original.

### Licenças permissivas (MIT, Apache 2.0, BSD)
- Pode modificar, redistribuir e até usar comercialmente
- Precisa manter o aviso de copyright/licença original no código (não apagar o nome do autor)
- Publicar como projeto derivado seu é permitido, desde que credite a origem

### Licenças copyleft (GPL, AGPL)
- Se modificar e distribuir/publicar, o projeto derivado também precisa ser open source sob a mesma licença
- Não é possível fechar o código como proprietário

### Sem licença declarada
- Por padrão, significa "todos os direitos reservados"
- Fazer fork é permitido tecnicamente, mas reutilizar/redistribuir como seu não tem permissão legal automática
- Mais seguro: usar como referência de estudo (entender a lógica, reescrever do zero) em vez de copiar

---

## Regra prática para o portfólio

Antes de adaptar algo de um fork para um projeto próprio:

1. Verificar a licença do repositório original
2. Se MIT/Apache → adaptar à vontade, creditando a origem (ex: comentário `# Baseado em usuario/repo, adaptado por mim`)
3. Se GPL/AGPL → manter o projeto derivado também open source
4. Se sem licença → tratar como material de estudo, não como base de código a reutilizar publicamente
